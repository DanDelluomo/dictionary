#!/usr/bin/env python

"""Build a Python dictionary of English words."""

# Import Standard Libary Packages
import pickle
import time

# Import project modules
from scrape_merriam_webster import merriam_webster_def

# Retrieve massive Unix system word list.
with open('../words.txt', 'r') as f:
   words_list = f.read().split()

word_dict = {}
for word in words_list:
    # Throttle to avoid overloading merriam-webster.com 
    time.sleep(0.1)
    try:
        word_dict[word] = merriam_webster_def(word)
        with open('../logs/def_successes', 'a') as f:
            f.write(f"Defined {word} successfully\n")
    except BaseException as e:
        with open('../logs/def_failures', 'a') as f:
            f.write(f"Didn't define {word}: {e}\n")

with open('dictionary.pickle', 'wb') as handle:
    pickle.dump(word_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)