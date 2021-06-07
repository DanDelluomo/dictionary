#!/usr/bin/env python

"""Build a Python dictionary of English words."""

# Import Standard Libary Packages
import pickle
import time

# Import project modules
from scrape_merriam_webster import merriam_webster_def

# Retrieve massive Unix system word list
with open('../words.txt', 'r') as f:
   words_list = f.read().split()

# Figure out last defined word  
with open('../logs/defs') as f:
    new_index = 0
    if len(f.readlines()) > 2:
        last_line = f.readlines()[-1]
        last_word = last_line.split(' ')[0]
        new_index = words_list.index(word) + 1

words_list = words_list[new_index:]

words_dict = {}
for word in words_list:
    # Slight throttle to avoid overloading merriam-webster.com 
    time.sleep(0.01)
    try:
        definition = merriam_webster_def(word)
        words_dict[word] = definition
        with open('../logs/defs', 'a') as f:
            f.write(f"{word} {definition}\n")
    except BaseException as e:
        with open('../logs/failures', 'a') as f:
            f.write(f"Couldn't define {word} due to: {e}\n")

with open('dict.pickle', 'wb') as handle:
    pickle.dump(words_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    