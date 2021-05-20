
# from tensorflow.keras.preprocessing.text import Tokenizer
# This doesn't line doesn't work on my computer: 
#   from tensorflow.keras.preprocessing.text import Tokenizer
# After repeated reinstalling of packages, I gave up and built my own tokenizer

def tokenizer(words_list: list) -> dict:
    """Tokenizes words in word_list"""
    words_index = dict()
    count = 1
    for word in words_list:
        if word not in words_index:
            words_index[count] = word
            count += 1
    return words_index

with open('../words.txt', 'r') as f:
   words_list = f.read().split()
   words_index = tokenizer(words_list)
    
# print(words_index)
    
