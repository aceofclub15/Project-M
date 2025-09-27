#!/usr/bin/env python3
"""
conversion_improved.py

Improved replacement script for inserting voice_line(...) calls into a Ren'Py
script based on a notes file containing voice-line codes.

This variant uses module-level variables for the input/output file paths and
flags instead of reading them from the command line. Edit the variables below
to set the files you want to process.

Features retained from the previous version:
- Robust parsing of notes lines (allows more flexible name tokens)
- Case-insensitive matching (normalizes to NFC and lower)
- Prefer longest snippet match when multiple snippets match
- Handles multiple quoted substrings per script line (inserts once per line)
- Writes unmatched notes lines to a separate file and prints them
- Optional inplace behavior (back up original to .bak)
- Logging for status messages

How to use:
- Edit the NOTES_FILE / SCRIPT_FILE / OUTPUT_FILE / UNMATCHED_FILE variables below
  to point to your files.
- Optionally toggle INPLACE or DEBUG.
- Then run:
    python conversion_improved.py

"""

from __future__ import annotations
import logging
import re
import sys
from pathlib import Path
import unicodedata
from typing import Dict, List, Tuple
import json

# ----------------------------- CONFIGURE HERE -----------------------------
# Edit these variables instead of passing command-line arguments.
NOTES_FILE = Path("notes.txt")
SCRIPT_FILE = Path("script.rpy")
OUTPUT_FILE = Path("01Processed.txt")
UNMATCHED_FILE = Path("unmatched_notes.txt")
INPLACE = False  # If True, original script will be moved to script.rpy.bak and overwritten
DEBUG = False
# How many recent non-blank lines to inspect for an existing identical voice_line
VOICE_LOOKBACK = 6
# Regex to strip Ren'Py inline text tags like {i}, {/i}, {b}, {color=#fff}, etc.
RENPI_TAG_RE = re.compile(r"\{.*?\}")

# -------------------------------------------------------------------------

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("conversion")

# Regex to parse notes lines. This is intentionally permissive regarding the
# 'name' token (it may contain spaces and punctuation) but requires the three
# underscore-separated codes at the start of the line.
NOTES_RE = re.compile(r'''^\s*(?P<p1>[^_\s]+)_(?P<p2>[^_\s]+)_(?P<p3>[^_\s]+)\s+(?P<name>.+?)\s+"(?P<snippet>.*)"\s*$''')

# Regex to find quoted strings in a script line (simple double-quote only)
QUOTED_RE = re.compile(r'"([^\"]*)"')


def normalize_text(s: str) -> str:
    """Normalize text for matching: strip Ren'Py tags, unicode NFC, lowercase, trim."""
    # Remove Ren'Py inline tags like {i}, {/i}, {b}, {color=#fff}, etc.
    s = RENPI_TAG_RE.sub("", s)
    return unicodedata.normalize("NFC", s).strip().lower()



def load_notes(notes_path: Path) -> Tuple[Dict[str, Tuple[str, str, str, str]], List[str]]:
    """
    Load and parse notes file.
    Returns:
      - dialogue_map: mapping normalized_snippet -> (p1,p2,p3, original_line)
      - unmatched_lines: list of original lines that failed to parse
    """
    dialogue_map: Dict[str, Tuple[str, str, str, str]] = {}
    unmatched: List[str] = []
    duplicates: List[str] = []

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
            snippet = m.group("snippet").strip()
            if not snippet:
                unmatched.append(f"{ln_no}: {line}  # empty snippet")
                continue

            norm = normalize_text(snippet)
            if norm in dialogue_map:
                duplicates.append(f"{ln_no}: duplicate snippet -> {snippet}")
                # We'll keep the first entry; log duplicate
                continue

            dialogue_map[norm] = (p1, p2, p3, line)

    if duplicates:
        logger.warning("Found duplicate snippets in notes.txt; keeping first occurrence(s):")
        for d in duplicates:
            logger.warning("  %s", d)

    return dialogue_map, unmatched


def build_sorted_snippets(dialogue_map: Dict[str, Tuple[str, str, str, str]]) -> List[str]:
    """Return the list of normalized snippets sorted by length desc (longest first)."""
    snippets = list(dialogue_map.keys())
    snippets.sort(key=len, reverse=True)
    return snippets


def detect_indentation(line: str) -> str:
    """Return the leading whitespace of a line (to respect indent when inserting)."""
    m = re.match(r"^(\s*)", line)
    return m.group(1) if m else ""


def make_voice_line(p1: str, p2: str, p3: str, indent: str = "    ") -> str:
    # Use json.dumps to safely produce quoted, escaped string literals
    return f"{indent}$ voice_line({json.dumps(p1)},{json.dumps(p2)},{json.dumps(p3)})\n"


def _recent_nonblank_lines(processed: List[str], limit: int) -> List[str]:
    """Return up to `limit` most recent non-blank lines from processed (in normal order)."""
    out: List[str] = []
    for ln in reversed(processed):
        if ln.strip():
            out.append(ln.rstrip("\n"))
            if len(out) >= limit:
                break
    return list(reversed(out))


def _already_has_voice_line(processed: List[str], voice_line_str: str, lookback: int) -> bool:
    """Return True if `voice_line_str` (stripped) appears in recent non-blank lines."""
    target = voice_line_str.strip()
    recent = _recent_nonblank_lines(processed, lookback)
    for r in recent:
        if r.strip() == target:
            return True
    return False

def _recent_has_any_voice_line(processed: List[str], lookback: int) -> bool:
    """Return True if any voice_line(...) call appears in recent non-blank lines."""
    recent = _recent_nonblank_lines(processed, lookback)
    for r in recent:
        if re.match(r'^\s*\$\s*voice_line\s*\(', r):
            return True
    return False
def process_script(script_path: Path, out_path: Path, dialogue_map: Dict[str, Tuple[str, str, str, str]],
                   snippets_sorted: List[str], inplace: bool = False) -> None:    
    """
    Read the script, insert voice_line before any line whose quoted text starts with
    a snippet from the notes file.
    Writes the processed script to out_path. If inplace=True, the original is backed up
    to script_path.with_suffix(script_path.suffix + '.bak') and the out_path will be
    the original script_path.
    """
    with script_path.open("r", encoding="utf-8") as fh:
        lines = fh.readlines()

    processed: List[str] = []
    inserted_count = 0

    for i, line in enumerate(lines):
        stripped = line.rstrip("\n")
        quoted = QUOTED_RE.findall(stripped)
        matched_for_line = False

        for q in quoted:
            norm_q = normalize_text(q)
            for snippet in snippets_sorted:
                if norm_q.startswith(snippet):
                    p1, p2, p3, original_note_line = dialogue_map[snippet]
                    indent = detect_indentation(line)
                    voice_line = make_voice_line(p1, p2, p3, indent)

                    # Avoid inserting duplicates or any voice_line already before this dialogue
                    if _recent_has_any_voice_line(processed, VOICE_LOOKBACK):
                        logger.debug(f"Skipping insertion for line {i+1}: a voice_line(...) call already exists nearby")
                        processed.append(line)
                    elif _already_has_voice_line(processed, voice_line, VOICE_LOOKBACK):
                        logger.debug(f"Skipping insertion for line {i+1}: identical voice_line already present nearby")
                        processed.append(line)
                    else:
                        processed.append(voice_line)
                        processed.append(line)
                        inserted_count += 1
                        logger.info(f"Inserted for line {i+1}: matched snippet '{snippet}' -> {p1}_{p2}_{p3}")

                    matched_for_line = True
                    break
            if matched_for_line:
                break

        if not matched_for_line:
            processed.append(line)

    # If inplace is requested, create a backup
    if inplace:
        bak = script_path.with_suffix(script_path.suffix + ".bak")
        script_path.replace(bak)  # move original -> backup
        logger.info(f"Backed up original script to {bak}")
        write_target = script_path
    else:
        write_target = out_path

    with write_target.open("w", encoding="utf-8") as fh:
        fh.writelines(processed)

    logger.info(f"Processing complete. Inserted {inserted_count} voice_line call(s).\nWrote output to: {write_target}")


def write_unmatched(unmatched: List[str], out_path: Path) -> None:
    if not unmatched:
        logger.info("No unmatched lines found in notes file.")
        return
    with out_path.open("w", encoding="utf-8") as fh:
        fh.write("# Lines from notes.txt that did not match the expected pattern\n")
        fh.write("# Format: line_number: original_line\n\n")
        for u in unmatched:
            fh.write(u + "\n")
    logger.info(f"Wrote {len(unmatched)} unmatched notes lines to: {out_path}")


def main() -> int:
    # Use module-level variables as configuration
    notes = NOTES_FILE
    script = SCRIPT_FILE
    out = OUTPUT_FILE
    unmatched_out = UNMATCHED_FILE
    inplace = INPLACE

    if DEBUG:
        logger.setLevel(logging.DEBUG)

    if not notes.exists():
        logger.error("Notes file not found: %s", notes)
        return 2
    if not script.exists():
        logger.error("Script file not found: %s", script)
        return 2

    dialogue_map, unmatched = load_notes(notes)
    if not dialogue_map:
        logger.error("No valid snippets were parsed from the notes file. Aborting.")
        write_unmatched(unmatched, unmatched_out)
        return 3

    snippets_sorted = build_sorted_snippets(dialogue_map)
    logger.info(f"Loaded {len(dialogue_map)} snippet(s) from notes (longest-first order used for matching).")

    try:
        process_script(script, out, dialogue_map, snippets_sorted, inplace=inplace)
    except Exception as e:
        logger.exception("Error while processing script: %s", e)
        return 1

    write_unmatched(unmatched, unmatched_out)
    if unmatched:
        logger.info("\nUnmatched notes lines (also saved to file):")
        for u in unmatched:
            logger.info("  %s", u)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
