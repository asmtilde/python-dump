#!/usr/bin/env python3
import os
import sys

def list_files_with_header(directory, output_file):
    file_paths = []
    for root, _, files in os.walk(directory):
        for name in files:
            abs_path = os.path.join(root, name)
            rel_path = os.path.relpath(abs_path, directory)
            file_paths.append(rel_path.replace("\\", "/"))
    
    file_paths.sort()

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# DO NOT DELETE\n")
        for path in file_paths:
            f.write(f"{path}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: <directory> <output_file>")
        sys.exit(1)
    directory = sys.argv[1]
    output_file = sys.argv[2]
    list_files_with_header(directory, output_file)
