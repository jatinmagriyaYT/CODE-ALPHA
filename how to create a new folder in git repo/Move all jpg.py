import os
import shutil

def move_jpg_files():
    source_folder = input("Enter source folder path: ")
    dest_folder = input("Enter destination folder path: ")
    
    # Create destination folder if it doesn't exist
    os.makedirs(dest_folder, exist_ok=True)
    
    moved_files = 0
    
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.jpg'):
            source_path = os.path.join(source_folder, filename)
            dest_path = os.path.join(dest_folder, filename)
            shutil.move(source_path, dest_path)
            moved_files += 1
            print(f"Moved: {filename}")
    
    print(f"\nDone! Moved {moved_files} JPG files to {dest_folder}")

# Run the function
move_jpg_files()