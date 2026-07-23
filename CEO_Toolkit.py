import os
import shutil
from datetime import datetime

# Folders
DOWNLOAD = os.path.expanduser("~/storage/shared/Download")
DOCS = os.path.expanduser("~/storage/shared/Documents/CEO_Docs")
PICS = os.path.expanduser("~/storage/shared/Pictures/CEO_Pics")
CODE = os.path.expanduser("~/CEO_Code")

# Make folders if they don't exist
for folder in [DOCS, PICS, CODE]:
    os.makedirs(folder, exist_ok=True)

print("=== CEO TOOLKIT v1.0 ===")
print("1. Organize Downloads")
print("2. Show System Info")
print("3. Exit")

choice = input("Pick: ")

if choice == "1":
    for file in os.listdir(DOWNLOAD):
        if file.endswith(('.pdf', '.docx', '.txt')):
            shutil.move(os.path.join(DOWNLOAD, file), os.path.join(DOCS, file))
        elif file.endswith(('.jpg', '.png', '.jpeg')):
            shutil.move(os.path.join(DOWNLOAD, file), os.path.join(PICS, file))
        elif file.endswith(('.py', '.sh', '.zip')):
            shutil.move(os.path.join(DOWNLOAD, file), os.path.join(CODE, file))
    print("Downloads organized!")

elif choice == "2":
    print(f"Date: {datetime.now()}")
    print(f"Storage: {os.popen('df -h').read()}")

print("Done CEO")
