import unicodedata


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def is_anagram(str1, str2):
    rtn = False
    str1 = ''.join(filter(str.isalpha, strip_accents(str1))).lower()
    str2 = ''.join(filter(str.isalpha, strip_accents(str2))).lower()
    if len(str1) == len(str2):
        rtn = True
        for char in str1:
            if char not in str2:
                rtn = False
                break

    return rtn


if __name__ == "__main__":
    print(is_anagram("tea", "tea"))
