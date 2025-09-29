import os

# Path to the folder containing your files
folder = r"audio\voices\j"  # change this to your actual path

for filename in os.listdir(folder):
    old_path = os.path.join(folder, filename)
    
    # Skip if it's not a file
    if not os.path.isfile(old_path):
        continue
    
    # Remove " Graham" from the filename (before extension)
    name, ext = os.path.splitext(filename)
    new_name = name.replace(" June", "") + ext
    new_path = os.path.join(folder, new_name)
    
    # Rename the file
    os.rename(old_path, new_path)
    print(f'Renamed: {filename} -> {new_name}')