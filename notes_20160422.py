import string

with open('fdf.txt', 'rt') as f:
    text = f.read
for symbol in string.punctuation:
    text = text.replace(symbol, " ")
words = text.split()
fr_dict = {}
for word in words:
    if word.lower() in fr_dict:
        fr_dict[word.lower()] += 1
    else:
        fr_dict[word.lower()] = 1
word_freq = [(counter, word) for word, counter in fr_dict.items()]
word_freq.sort()
print(word_freq)
