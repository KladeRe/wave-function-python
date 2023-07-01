import os

# This gives all files
def find_files(directory):
    files_found = []
    for path, subdirs, files in os.walk(directory):
        for name in files:
            files_found.append(os.path.join(path, name))
    return files_found

