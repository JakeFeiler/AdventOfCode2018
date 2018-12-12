#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import sys
import string

def getText(inputText):
    text = open(inputText,'r')
    lines = [line.strip().split(' ') for line in text]
    return lines



def getOrder(text):
    """Create an array tracking the immediate dependencies for every letter"""
    """Loop through while there still exist dependencies, do the first element with no dependencies left"""
    dependencies = [' ']*26
    finalOrder = ''
    alphaDict = {k: v for  v, k in enumerate(string.ascii_uppercase)}
    
    #Value v at position p in dependencies: steps v to be completed before p
    for line in text:
        dependencies[alphaDict[line[7]]] += line[1]

    #26 iterations sufficient to find order, remove 'no dependencies', update rest accordingly
    for x in range(26):
        for value, dependency in enumerate(dependencies):
            if dependency == ' ':
                finalOrder += string.ascii_uppercase[value]
                dependencies[value] = '0'
                #Remove all instances of the corresponding letter from all dependencies
                for y in range(26):
                    dependencies[y] = dependencies[y].replace(string.ascii_uppercase[value], '')
                break
            
    return finalOrder

lines = getText('input.txt')
print(getOrder(lines))
