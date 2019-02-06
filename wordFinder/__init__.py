from nltk.corpus import wordnet
from itertools import permutations
import warnings


def wordFinder(scrabble_str, blanks=-1):
    if blanks > 2:
        blanks = 2
    str_list = []
    temp_str = ''
    if blanks == 2:
        for i in range(26):
            for j in range(26):
                temp_str = scrabble_str + chr(ord('a') + j) + chr(ord('a') + i)
                str_list.append(temp_str)
                # print(temp_str)
    elif blanks == 1:
        for j in range(26):
            temp_str = scrabble_str + chr(ord('a') + j)
            str_list.append(temp_str)
            # print(temp_str)
    else:
        str_list.append(scrabble_str)
    str_list = set(str_list)
    for string in str_list:
        checkAllPermutations(string)
    print(str(count) + ' words found')


def checkAllPermutations(scrabble_str):
    global count
    # Get all permutations of string 'ABC'
    permList = permutations(scrabble_str)
    temp = ''
    # print all permutations
    for perm in list(permList):
        temp = ''.join(perm)
        if wordnet.synsets(temp):
            count += 1
            print(temp)


count = 0
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    wordFinder('able', 0)
