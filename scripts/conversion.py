import sys
import re
from typing import Dict, List, Tuple

def create_dialogue_map(notes_file_path: str) -> Dict[str, Tuple[str, str, str]]:
    """
    Reads the notes.txt file and creates a dictionary mapping partial dialogue 
    (key) to a tuple containing (char_code, emotion_code, tone_code) for the 
    voice_line function call.
    """
    dialogue_map = {}
    
    # Regex to capture the codes and the quoted dialogue:
    # 1. (\w{1,2}) - Captures char code (e.g., 'm' or 'gm')
    # 2. (\w+) - Captures the emotion part (e.g., 'ah')
    # 3. (\w+) - Captures the tone part (e.g., 'hap')
    # 4. "([^"]*)" - Captures the partial dialogue inside quotes
    # The whole pattern: ^(?P<p1>\w{1,2})_(?P<p2>\w+)_(?P<p3>\w+)\s+[\w"]+\s+"(?P<dialogue>[^"]*)"$
    pattern = re.compile(r'^(?P<p1>\w{1,2})_(?P<p2>\w+)_(?P<p3>\w+)\s+[\w"]+\s+"(?P<dialogue>[^"]*)"$')
    
    try:
        with open(notes_file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                match = pattern.search(line)
                if match:
                    # Get the dialogue snippet and normalize it (strip spaces)
                    dialogue_snippet = match.group('dialogue').strip()
                    
                    # Store the voice codes (p1=char, p2=emotion, p3=tone)
                    voice_codes = (
                        match.group('p1'), 
                        match.group('p2'), 
                        match.group('p3')
                    )
                    dialogue_map[dialogue_snippet] = voice_codes
    except FileNotFoundError:
        print(f"Error: Notes file not found at {notes_file_path}")
        sys.exit(1)
        
    return dialogue_map

# -----------------------------------------------------------------------------

def process_script(script_file_path: str, dialogue_map: Dict[str, Tuple[str, str, str]]) -> List[str]:
    """
    Reads the script file, finds dialogue lines matching the map, and 
    inserts the voice_line call before them.
    """
    # CORRECTED: Initialize processed_lines as an empty list
    processed_lines = [] 
    
    # Regex to capture any quoted text in a line
    dialogue_pattern = re.compile(r'"([^"]*)"') 
    
    try:
        with open(script_file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # Always append the current line first
                processed_lines.append(line) 
                
                # Check for dialogue in the line
                match = dialogue_pattern.search(line)
                if match:
                    # Get the full dialogue string and normalize it
                    full_dialogue = match.group(1).strip()
                    
                    # Iterate through the dialogue map to find a match
                    for snippet, (p1, p2, p3) in dialogue_map.items():
                        # Check if the full dialogue line STARTS with the partial snippet
                        if full_dialogue.startswith(snippet):
                            # The voice line call must be inserted *before* the dialogue,
                            # so we insert it at the position *before* the current line.
                            # Since we already appended the current line, we must remove it,
                            # insert the voice line, and then re-append the current line.
                            
                            # Remove the line we just appended
                            processed_lines.pop() 
                            
                            # Construct the voice line call with 4 spaces for Ren'Py indentation
                            voice_line = f'    $ voice_line("{p1}","{p2}","{p3}")\n'
                            
                            # Insert the voice line
                            processed_lines.append(voice_line)
                            
                            # Re-append the original line
                            processed_lines.append(line)
                            
                            # Break the inner loop once a match is found
                            break 
                            
    except FileNotFoundError:
        print(f"Error: Script file not found at {script_file_path}")
        sys.exit(1)
        
    return processed_lines

# -----------------------------------------------------------------------------

def main():
    """Main function to orchestrate the conversion process."""

        
    # CORRECTED: Use correct sys.argv indices
    notes_file_path = "notes.txt"
    script_file_path = "scene_stop_sarah_assassination.rpy"
    output_file_path = "01Processed.rpy"
    
    print(f"1. Creating dialogue map from: {notes_file_path}")
    dialogue_map = create_dialogue_map(notes_file_path)
    print(f"   -> Found {len(dialogue_map)} voice lines to insert.")

    print(f"2. Processing script file: {script_file_path}")
    processed_lines = process_script(script_file_path, dialogue_map)

    print(f"3. Writing output to: {output_file_path}")
    try:
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.writelines(processed_lines)
        print("✅ Conversion complete!")
    except IOError:
        print(f"Error: Could not write to output file at {output_file_path}")
        sys.exit(1)

if __name__ == "__main__":
    main()