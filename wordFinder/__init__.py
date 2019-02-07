from itertools import permutations, combinations
from nltk.corpus import wordnet
import warnings


def word_finder(scrabble_str, blanks=-1, prefix="", suffix=""):
    if blanks > 2:
        blanks = 2
    str_list = []
    if blanks == 2:
        for i in range(26):
            for j in range(26):
                temp_str = scrabble_str + chr(ord('a') + j) + chr(ord('a') + i)
                str_list.append(temp_str)
    elif blanks == 1:
        for j in range(26):
            temp_str = scrabble_str + chr(ord('a') + j)
            str_list.append(temp_str)
    else:
        str_list.append(scrabble_str)
    str_list = set(str_list)
    for string in str_list:
        check_all_permutations(string, prefix, suffix)


def check_all_permutations(scrabble_str, prefix="", suffix=""):
    global count
    global word_list
    count = 0
    # Get all permutations of string 'ABC'
    perm_list = permutations(scrabble_str)
    perm_list = [(prefix + ''.join(x) + suffix) for x in perm_list]
    # print all permutations
    for perm in set(perm_list):
        if wordnet.synsets(perm):
            word_list.append(perm)


def find_all_words(all_chars, blanks=0, prefix="", suffix="", min_chars=1):
    if min_chars > len(all_chars):
        raise ValueError("min_chars should be lesser than number of characters in all_chars")

    all_combinations = []
    for i in range(min_chars, len(all_chars) + 1):
        all_combinations.extend([''.join(x) for x in combinations(all_chars, i)])
    for combo in all_combinations:
        word_finder(combo, blanks, prefix, suffix)


count = 0
word_list = []
find_all_words("slaus", blanks=0, prefix="a", suffix="t", min_chars=3)
word_list = set(word_list)

for word in word_list:
    print(word)
print(str(len(word_list)) + ' words found')
