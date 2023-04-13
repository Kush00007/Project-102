import os
import shutil

from_dir = os.path.expanduser("E:/Downloads")
to_dir = os.path.expanduser("E:/Document_Files")

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, ext = os.path.splitext(file_name)
    if not ext:
        continue
    if ext in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, ext[1:].upper() + "_Files")
        path3 = os.path.join(path2, file_name)
        if not os.path.exists(path2):
            os.makedirs(path2)
            print(f"Created directory: {path2}")
        print(f"Moving {file_name} to {path2}")
        shutil.move(path1, path3)
