import string
import re

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']


def count_words(sentences):
    rv = {}
    # sentences = sentences.translate(str.maketrans('', '', string.punctuation)).lower()
    # sentences = re.sub(r'[\W_]+', '', sentences.lower())
    sentences = sentences.lower()
    lst = sentences.split(' ')
    for word in lst:
        if word[0] not in chars:
            word = word[1:]
        if word[-1] not in chars:
            word = word[0:-1]
        if word in rv:
            rv[word] += 1
        else:
            rv[word] = 1
    return rv


if __name__ == '__main__':
    count = count_words("oh. what. a day what a lovely day!")
    print(count)
