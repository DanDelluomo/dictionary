from scrape_merriam_webster import merriam_webster_def

word_list = ['ass', 'bill', 'car', 'dog', 'love', 'mole', 'sex', 'zoo']

word_dict = {}
for word in word_list:
    try:
        word_dict[word] = merriam_webster_def(word)
    except:
        pass

print(word_dict)
