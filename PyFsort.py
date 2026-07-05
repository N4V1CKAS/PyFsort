import os
import shutil

dir_path = (input("Enter your desired directory: "))

with os.scandir(dir_path) as files:
    for entry in files:
        if entry.is_file():
            filename, extensions = os.path.splitext(entry.name)
            extensions = extensions.lower()
            
            folder_path = os.path.join(dir_path, extensions)
            
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                
            dest = os.path.join(folder_path, entry.name)
            
            if not os.path.exists(dest):
                shutil.move(entry.path, folder_path)
                print("Moved: " + entry.name)
            else:
                print("Skipped (already exists): " + entry.name)
