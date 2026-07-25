import os
import shutil

print("=== CEO FILE ORGANIZER v1.0 ===")
print("I will clean your storage automatically\n")

path = input("Enter folder to clean. Example: storage/downloads: ")

file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Apps': ['.apk']
}

for folder in file_types:
    if not os.path.exists(os.path.join(path, folder)):
        os.makedirs(os.path.join(path, folder))

files = os.listdir(path)
moved = 0

for file in files:
    for folder, extensions in file_types.items():
        if any(file.endswith(ext) for ext in extensions):
            shutil.move(os.path.join(path, file), os.path.join(path, folder, file))
            moved += 1
            break

print(f"\nDONE! Moved {moved} files.")
print("Your folder is now clean CEO!")
