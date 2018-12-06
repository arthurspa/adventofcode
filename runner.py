import sys
import os
import importlib

year_folder, filename = sys.argv[1].split('/')
filename = filename.split('.')[0]

module = importlib.import_module(f'{year_folder}.{filename}')

if getattr(module, 'solve', False):
    with open(f'{year_folder}/input/{filename}') as read:
        module.solve(read)
else:
    print('Missing solve function?')
