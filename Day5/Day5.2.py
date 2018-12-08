#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import sys
from string import ascii_lowercase

def getText(text):
    f = open(text, 'r')
    word = f.read()
    f.close()
    return word.strip()

#Remove all instances of letter 'character' from word 'polymer'
def shorten(character, polymer):
    shortenedPolymer = ''
    for letter in polymer:
        if letter.upper() != character.upper():
            shortenedPolymer += letter
    return shortenedPolymer

def destroy(word):
    simple = ''
    for letter in word:
        if len(simple) == 0:
            simple += letter
        #If the last character of simple has opposite polarity to letter, kill it
        elif simple[-1:].upper() == letter.upper() and simple[-1:] != letter:
            simple = simple[0:-1]
        #Otherwise no match, just add the letter to the simplified polymer
        else:
            simple += letter
    return len(simple)


def main():
    polymer = getText('input.txt')
    minLength = len(polymer)
    for c in ascii_lowercase:
        length = destroy(shorten(c,polymer))
        if length < minLength:
            minLength = length
    print(minLength)

if __name__ == "__main__":
    main()
