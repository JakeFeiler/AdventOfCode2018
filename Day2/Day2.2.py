#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import sys
import itertools

def getText(text):
    ids = []
    f = open(text, 'r')
    for line in f:
        line=line.strip()
        ids.append(line)
    ids.sort()
    return ids

#Hope the first letter works is a match, I'll see what happens
#Done to reduce number of required iterations
def checkByFirstLetter(ids):
    for key, group in itertools.groupby(ids, lambda x: x[0]):
        attemptMatch(list(group))

#Check to see if 2 words match
def attemptMatch(subIds):
    for index1 in range(0,len(subIds)):
        for index2 in range(index1 + 1, len(subIds)):
            compare(subIds[index1], subIds[index2])

#Count the number of differences between 2 words, return if there is only 1 difference
def compare(word1, word2):
    count = 0
    for l in range(0,len(word1)):
        if (word1[l] == word2[l]):
            count += 1
    if (count == len(word1)-1):
        print(word1, word2)
        

ids = getText('input.txt')
checkByFirstLetter(ids)

