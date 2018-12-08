#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import sys
from string import ascii_lowercase

def getText(text):
    ids = []
    f = open(text, 'r')
    for line in f:
        line=line.strip()
        ids.append(line)
    return ids

def countDoublesTimesTriples(ids):
    count2 = 0
    count3 = 0
    LETTERS = {letter: index for index, letter in enumerate(ascii_lowercase, start=0)}
    #Track the count of every letter in a word with a list of length 26
    for word in ids:
        lettercount = [0]*26
        for character in word:
            lettercount[LETTERS[character]] += 1
        for letter in lettercount:
            if (letter == 2):
                count2 +=1
                break
        for letter in lettercount:
            if (letter == 3):
                count3 += 1
                break
    return count2*count3

idNumbers = getText('input.txt')
print(countDoublesTimesTriples(idNumbers))

