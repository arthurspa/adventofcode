import sys
import os
import importlib

year_folder, filename = sys.argv[1].split("/")
filename = filename.split(".")[0]

module = importlib.import_module(f"{year_folder}.{filename}")

if getattr(module, "solve", False):
    file_path = f"{year_folder}/input/{filename}"
    if not os.path.isfile(file_path):
        file_path = file_path.split("_")[0]  # remove _1 or _2

    if not os.path.isfile(file_path):
        print("Missing input file?")
    else:
        with open(file_path) as read:
            module.solve(read)
else:
    print("Missing solve function?")
