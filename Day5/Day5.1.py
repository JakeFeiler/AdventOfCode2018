#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3                                                                
 
import sys

def getText(text):
    f = open(text, 'r')
    word = f.read()
    f.close()
    return word.strip()

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
                
        
        
        
polymer = getText('input.txt')
print(destroy(polymer))
