import re
from typing import Dict, List, Tuple

def parse_voice_notes(notes_file_path: str) -> Dict[Tuple[str, str], str]:
    """
    Parses the notes file to create a mapping from a (Speaker, Partial Dialogue) 
    tuple to the voice line function call.
    """
    voice_map = {}
    
    # Regex to capture the codes, speaker name, and the partial dialogue inside quotes.
    line_pattern = re.compile(r'^(?P<vcode>[a-z0-9]{1,3})_(?P<codes>[a-z]{2}_[a-z]{3})\s+(?P<speaker>\w+)\s+"(?P<dialogue_phrase>.*?)"\s*$', re.MULTILINE)

    try:
        with open(notes_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Notes file not found at {notes_file_path}")
        return voice_map

    for match in line_pattern.finditer(content):
        speaker_code = match.group(1)
        codes = match.group('codes') 
        speaker_name = match.group('speaker') 
        dialogue_phrase = match.group('dialogue_phrase').strip() 

        try:
            emotion, tone = codes.split('_')
        except ValueError:
            print(f"Skipping malformed code in line: {match.group(0)}")
            continue

        voice_line_call = f'$ voice_line("{speaker_code}","{emotion}","{tone}")'

        # The key is a tuple: (SpeakerName, Unique Phrase)
        voice_map[(speaker_name, dialogue_phrase)] = voice_line_call

    return voice_map

# ----------------------------------------------------------------------

def insert_voice_lines(script_file_path: str, output_file_path: str, voice_map: Dict[Tuple[str, str], str]):
    """
    Reads the script file, finds the full dialogue line containing the phrase, 
    inserts the voice line calls *before* the dialogue line, and writes the 
    result to a new file.
    """
    try:
        with open(script_file_path, 'r', encoding='utf-8') as f:
            script_lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: Script file not found at {script_file_path}")
        return

    modified_lines = []
    lines_inserted = 0
    
    # Regex for a dialogue line: captures speaker and the full dialogue content
    dialogue_pattern = re.compile(r'^\s*(?P<speaker>\w+)\s+"(?P<dialogue>.+?)"\s*$', re.MULTILINE)

    for i, line in enumerate(script_lines):
        match = dialogue_pattern.match(line)
        
        # Check if the line is a dialogue line that needs a voice tag
        if match:
            speaker_name = match.group('speaker')
            dialogue = match.group('dialogue')
            
            # Check every entry in the voice_map for a match
            for (map_speaker, map_phrase), voice_line_call in voice_map.items():
                if speaker_name == map_speaker and map_phrase in dialogue:
                    
                    # Determine the indentation of the original line
                    indentation = len(line) - len(line.lstrip())
                    
                    # 1. Construct the voice line call with correct indentation
                    voice_line_to_insert = f"{' ' * indentation}{voice_line_call}\n"
                    
                    # 2. INSERT THE VOICE LINE *BEFORE* the dialogue line
                    modified_lines.append(voice_line_to_insert)
                    lines_inserted += 1
                    
                    # Break the inner loop once a match is found
                    break 

        # Now, add the original dialogue line (or non-dialogue line)
        modified_lines.append(line)


    # Write the modified content
    try:
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.writelines(modified_lines)
        print(f"\n✅ Successfully converted script written to: {output_file_path}")
        print(f"Total voice lines inserted: {lines_inserted}")
    except Exception as e:
        print(f"Error writing output file: {e}")

# --- Main execution ---
if __name__ == "__main__":
    # Define file paths
    notes_path = "notes.txt"
    script_path = "script.rpy" 
    output_path = "script_with_voice_partial_corrected.txt" # Changed output name to avoid overwriting

    print(f"1. Parsing voice notes from: {notes_path}")
    voice_map = parse_voice_notes(notes_path)

    if voice_map:
        print(f"2. Voice map created with {len(voice_map)} entries for partial matching.")
        
        print(f"3. Inserting voice lines into: {script_path}")
        insert_voice_lines(script_path, output_path, voice_map)
    else:
        print("No voice lines found or error occurred during parsing. Conversion aborted.")