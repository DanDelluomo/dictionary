#!/usr/bin/env python

"""Build a Python dictionary of English words."""

# Import Standard Libary Packages
import pickle
import time
import pathlib

parent_path = pathlib.Path(__file__).absolute().parents[1] 
words_path = parent_path / "tools" / "words.txt"
defs_path = parent_path / "defs_test"
failures_path = parent_path / "logs" / "failures"

# Import project modules
from scrape_merriam_webster import merriam_webster_def

# Retrieve massive Unix system word list
with open(words_path, 'r') as f:
   words_list = f.read().split()

# Figure out last defined word  
with open(defs_path) as f:
    new_index = 0
    whole_file = f.readlines()
    if len(whole_file) > 2:
        last_line = whole_file[-1]
        last_word = last_line.split(' ')[0]
        new_index = words_list.index(last_word) + 1

words_list = words_list[new_index:]

words_dict = {}
for word in words_list:
    # Slight throttle to avoid overloading merriam-webster.com 
    time.sleep(0.01)
    try:
        definition = merriam_webster_def(word)
        words_dict[word] = definition
        with open(defs_path, 'a') as f:
            f.write(f"{word} {definition}\n")
    except BaseException as e:
        with open(failures_path, 'a') as f:
            f.write(f"Couldn't define {word} due to: {e}\n")

# with open('dict.pickle', 'wb') as handle:
#     pickle.dump(words_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    