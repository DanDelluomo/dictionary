#!/usr/bin/env python

"""
The statement: from tensorflow.keras.preprocessing.text import Tokenizer
doesn't work on my laptop for some reason. After repeated attempts to fix this apparently environment-related error, I decided to simply build a tokenizer myself.
"""

import pathlib 

parent_path = pathlib.Path(__file__).absolute().parents[1] 
words_path = parent_path / "tools" / "words.txt"

def tokenizer(words_list: list) -> dict:
    """Tokenizes words in word_list"""
    words_index = dict()
    count = 1
    for word in words_list:
        if word not in words_index:
            words_index[count] = word
            count += 1
    return words_index

with open(words_path, 'r') as f:
   words_list = f.read().split()
   words_index = tokenizer(words_list)
    
# print(words_index)
    
