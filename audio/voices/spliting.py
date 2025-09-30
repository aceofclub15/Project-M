import os

# Path to the folder containing the wav files
folder = r"audio\voices\s"  # change this to your actual path
output_file = "voice_lines.txt"

with open(output_file, "w", encoding="utf-8") as f:
    for filename in os.listdir(folder):
        if filename.endswith(".wav"):
            name = os.path.splitext(filename)[0]  # remove .wav
            parts = name.split("_")
            
            if len(parts) == 3:
                char, sound, emotion = parts
                line = f'$ voice_line("{char}", "{sound}", "{emotion}")\n'
                f.write(line)
                print(line.strip())
            else:
                print(f"Skipped: {filename} (unexpected format)")
