#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, shutil, sys

sys.stdout.reconfigure(encoding='utf-8')

# Get all files in Clippings that we want to move (Turkish files with apostrophes)
clippings_dir = 'Clippings'
raw_dir = 'raw'

files_to_move = [f for f in os.listdir(clippings_dir) if f not in os.listdir(raw_dir)]

# Only move the 5 specific files we processed
target_names = [
    "Dünya'nın",
    "Kıyamet",
    "Trump'ın",
    "Küresel",
    "savaşı'ında"
]

moved = 0
for f in files_to_move:
    for t in target_names:
        if t in f:
            src = os.path.join(clippings_dir, f)
            dst = os.path.join(raw_dir, f)
            shutil.move(src, dst)
            print(f'Moved: {f}')
            moved += 1
            break

print(f'\nTotal moved: {moved}')
