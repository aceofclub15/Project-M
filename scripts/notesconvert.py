#!/usr/bin/env python3
"""
notesconvert.py  (patched)

- Requires speaker match by default, but has a safe fallback to single-candidate matches.
- Strips Ren'Py inline tags before matching.
- Fixes replacement by using indices for recent non-blank lines.
- Logs why snippet matches were skipped (enable DEBUG to see).
"""

from __future__ import annotations
import logging
import re
from pathlib import Path
import unicodedata
from typing import Dict, List, Tuple, Optional
import json

# ---------------- CONFIG ----------------
NOTES_FILE = Path("notes_cleaned.txt")
SCRIPT_FILE = SCRIPT_FILES = [
    Path("scene_grandmaster_ending.rpy"),



]

#OUTPUT_FILE = Path("01Processed.txt")
UNMATCHED_FILE = Path("unmatched_notes.txt")
INPLACE = False
DEBUG = True            # set True while testing to see debug logs
VOICE_LOOKBACK = 1      # how many recent nonblank lines to inspect for duplication/replacement
FALLBACK_SINGLE_CANDIDATE_IF_NO_SPEAKER = True  # if True, match single candidate even when speaker not found
# ----------------------------------------

logging.basicConfig(level=logging.DEBUG if DEBUG else logging.INFO, format="%(message)s")
logger = logging.getLogger("notesconvert")

# Regexes
NOTES_RE = re.compile(r'^\s*(?P<p1>[^_\s]+)_(?P<p2>[^_\s]+)_(?P<p3>[^_\s]+)\s+(?P<name>.+?)\s+"(?P<snippet>.*)"\s*$')
# accept double or single quoted dialogue
QUOTED_RE = re.compile(r'["\']([^"\']*)["\']')
# strip renpy inline tags
RENPY_TAG_RE = re.compile(r'\{.*?\}')
VOICE_LINE_CALL_RE = re.compile(r'^\s*\$\s*voice_line\s*\(')


def normalize_text(s: Optional[str]) -> str:
    if s is None:
        return ""
    # remove inline renpy tags like {i}{/i} and normalize
    s2 = RENPY_TAG_RE.sub("", s)
    return unicodedata.normalize("NFC", s2).strip().lower()


def load_notes(notes_path: Path) -> Tuple[Dict[str, List[Tuple[str, str, str, str]]], List[str]]:
    dialogue_map: Dict[str, List[Tuple[str, str, str, str]]] = {}
    unmatched: List[str] = []
    if not notes_path.exists():
        logger.error("Notes file not found: %s", notes_path)
        return dialogue_map, unmatched

    with notes_path.open("r", encoding="utf-8") as fh:
        for ln_no, raw in enumerate(fh, start=1):
            line = raw.rstrip("\n")
            if not line.strip():
                continue
            m = NOTES_RE.match(line)
            if not m:
                unmatched.append(f"{ln_no}: {line}")
                continue
            p1 = m.group("p1").strip()
            p2 = m.group("p2").strip()
            p3 = m.group("p3").strip()
            name = m.group("name").strip()
            snippet = m.group("snippet").strip()
            if not snippet:
                unmatched.append(f"{ln_no}: {line}  # empty snippet")
                continue
            norm = normalize_text(snippet)
            dialogue_map.setdefault(norm, []).append((p1, p2, p3, name))
    return dialogue_map, unmatched


def build_sorted_snippets(dialogue_map: Dict[str, List[Tuple[str, str, str, str]]]) -> List[str]:
    lst = list(dialogue_map.keys())
    lst.sort(key=len, reverse=True)
    return lst


def detect_indentation(line: str) -> str:
    m = re.match(r'^(\s*)', line)
    return m.group(1) if m else ""


def make_voice_line(p1: str, p2: str, p3: str, indent: str = "    ") -> str:
    return f'{indent}$ voice_line({json.dumps(p1)},{json.dumps(p2)},{json.dumps(p3)})\n'


def _recent_nonblank_indices(processed: List[str], limit: int) -> List[int]:
    indices: List[int] = []
    for idx in range(len(processed) - 1, -1, -1):
        if processed[idx].strip():
            indices.append(idx)
            if len(indices) >= limit:
                break
    return list(reversed(indices))


def _recent_nonblank_lines(processed: List[str], limit: int) -> List[str]:
    idxs = _recent_nonblank_indices(processed, limit)
    return [processed[i].rstrip("\n") for i in idxs]


def _already_has_voice_line(processed: List[str], voice_line_str: str, lookback: int) -> bool:
    target = voice_line_str.strip()
    recent = _recent_nonblank_lines(processed, lookback)
    for r in recent:
        if r.strip() == target:
            return True
    return False


def _is_voice_line(line: str) -> bool:
    if not line:
        return False
    return bool(VOICE_LINE_CALL_RE.match(line))


def _extract_voice_params(line: str) -> Optional[Tuple[str, str, str]]:
    if not _is_voice_line(line):
        return None
    qs = QUOTED_RE.findall(line)
    if len(qs) >= 3:
        return qs[0], qs[1], qs[2]
    return None


def _normalize_speaker_token(tok: str) -> str:
    return normalize_text(tok)


def process_script(script_path: Path, out_path: Path, dialogue_map: Dict[str, List[Tuple[str, str, str, str]]], snippets_sorted: List[str], inplace: bool = False) -> None:
    
    if not script_path.exists():
        logger.error("Script file not found: %s", script_path)
        return

    with script_path.open("r", encoding="utf-8") as fh:
        lines = fh.readlines()

    processed: List[str] = []
    inserted_count = 0
    updated_count = 0

    for i, line in enumerate(lines):
        stripped = line.rstrip("\n")
        quoted = QUOTED_RE.findall(stripped)
        if not quoted:
            processed.append(line)
            continue

        first_quoted = quoted[0]
        norm_quoted = normalize_text(first_quoted)

        # extract speaker token (part before first quote)
        first_quote_pos = re.search(r'["\']', line)
        speaker_token = ""
        if first_quote_pos:
            before = line[: first_quote_pos.start()].strip()
            if before:
                msp = re.search(r'([A-Za-z_][A-Za-z0-9_]*)\s*$', before)
                if msp:
                    speaker_token = msp.group(1)
                else:
                    speaker_token = before.split()[-1]
        speaker_norm = _normalize_speaker_token(speaker_token)

        matched_for_line = False

        # iterate snippets (longest-first)
        for snippet in snippets_sorted:
            if not norm_quoted.startswith(snippet):
                continue

            candidates = dialogue_map.get(snippet, [])
            if not candidates:
                # snippet found in script but not in notes (shouldn't happen here)
                continue

            # choose candidate by strict speaker match (unless fallback config allows a single-candidate match)
            chosen: Optional[Tuple[str, str, str, str]] = None
            if speaker_norm:
                for (p1, p2, p3, name) in candidates:
                    if speaker_norm == normalize_text(p1) or speaker_norm == normalize_text(name):
                        chosen = (p1, p2, p3, name)
                        break
            else:
                # no speaker detected — consider safe fallback if there's exactly one candidate
                if FALLBACK_SINGLE_CANDIDATE_IF_NO_SPEAKER and len(candidates) == 1:
                    chosen = candidates[0]
                    logger.debug(f"Line {i+1}: no speaker token but single candidate fallback used for snippet '{snippet}'")
                else:
                    logger.debug(f"Line {i+1}: no speaker token; skipping snippet '{snippet}'")

            if not chosen:
                # debug: show why we skipped
                cdbg = ", ".join([f"p1={normalize_text(x[0])}|name={normalize_text(x[3])}" for x in candidates])
                logger.debug(f"Line {i+1}: snippet matched text but no candidate matched speaker '{speaker_token}' (norm='{speaker_norm}'). Candidates: {cdbg}")
                continue

            # chosen exists -> insert/update voice_line
            p1, p2, p3, name = chosen
            indent = detect_indentation(line)
            voice_line = make_voice_line(p1, p2, p3, indent)

            # check nearby lines for existing voice_line (replacement) or identical duplicates
            recent_idxs = _recent_nonblank_indices(processed, VOICE_LOOKBACK)
            replaced = False
            if recent_idxs:
                closest_idx = recent_idxs[-1]
                closest_line = processed[closest_idx]
                if _is_voice_line(closest_line):
                    params = _extract_voice_params(closest_line)
                    if params:
                        existing_p1 = params[0]
                        if normalize_text(existing_p1) in {normalize_text(p1), normalize_text(name), speaker_norm}:
                            # replace existing (notes take priority)
                            processed[closest_idx] = voice_line
                            replaced = True
                            updated_count += 1
                            logger.info(f"Updated existing voice_line above line {i+1} -> {p1}_{p2}_{p3}")

            if not replaced:
                if _already_has_voice_line(processed, voice_line, VOICE_LOOKBACK):
                    logger.debug(f"Skipping insertion for line {i+1}: identical voice_line already present nearby")
                else:
                    processed.append(voice_line)
                    inserted_count += 1
                    logger.info(f"Inserted new voice_line for line {i+1} -> {p1}_{p2}_{p3}")

            processed.append(line)
            matched_for_line = True
            break  # stop checking more snippets for this dialogue

        if not matched_for_line:
            processed.append(line)

    # write output
    if inplace:
        bak = script_path.with_suffix(script_path.suffix + ".bak")
        script_path.replace(bak)
        logger.info(f"Backed up original script to {bak}")
        write_target = script_path
    else:
        write_target = out_path

    with write_target.open("w", encoding="utf-8") as fh:
        fh.writelines(processed)

    logger.info(f"Processing complete. Inserted {inserted_count} new voice_line(s), updated {updated_count} existing one(s). Output -> {write_target}")


def write_unmatched(unmatched: List[str], out_path: Path) -> None:
    if not unmatched:
        logger.info("No unmatched lines found in notes file.")
        return
    with out_path.open('w', encoding='utf-8') as fh:
        fh.write("# Lines from notes.txt that did not match the expected pattern\n")
        fh.write("# Format: line_number: original_line\n\n")
        for u in unmatched:
            fh.write(u + "\n")
    logger.info(f"Wrote {len(unmatched)} unmatched notes lines to: {out_path}")


def main() -> int:
    dialogue_map, unmatched = load_notes(NOTES_FILE)
    if not dialogue_map:
        logger.error("No valid snippets parsed from notes file.")
        write_unmatched(unmatched, UNMATCHED_FILE)
        return 2

    snippets_sorted = build_sorted_snippets(dialogue_map)
    logger.info(f"Loaded {len(dialogue_map)} snippet(s) from notes.txt")

    for script_file in SCRIPT_FILES:
        print(f"WORKING WITH THIS SCRIPT: {script_file}\n")
        output_file = script_file.with_name(f"{script_file.stem}_processed.txt")
        process_script(script_file, output_file, dialogue_map, snippets_sorted, inplace=INPLACE)

    write_unmatched(unmatched, UNMATCHED_FILE)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
