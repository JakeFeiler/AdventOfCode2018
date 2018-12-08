#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import sys

def getText(text):
    ids = []
    f = open(text, 'r')
    for line in f:
        f = line.strip()
        ids.append(line.split())
    return ids

def findUniqueElf(lines):
    dims = maxSize(lines)
    fabric = [0]*dims[0]
    for i in range(dims[0]):
        fabric[i] = [0]*dims[1]
    for elf in lines:
        corner = elf[2].split(',')
        left = int(corner[0])
        top = int(corner[1][:-1])
        dimensions = elf[3].split('x')
        for i in range(0, int(dimensions[0])):
            for j in range(0, int(dimensions[1])):
                fabric[left + i][top + j] +=1
    #Same code as 3.1 works, just now also check each elf on the matrix
    #See if every square they use has value=1 on fabric
    for elf in lines:
        hasNotOverlapped = True
        elfId = elf[0][1:]
        corner = elf[2].split(',')
        left = int(corner[0])
        top = int(corner[1][:-1])
        dimensions = elf[3].split('x')
        for i in range(0, int(dimensions[0])):
            for j in range(0, int(dimensions[1])):
                if fabric[left + i][top + j] != 1:
                    hasNotOverlapped = False
        if hasNotOverlapped == True:
            return elfId

def maxSize(lines):
    left  = 0
    top = 0
    width = 0
    height = 0
    for elf in lines:
        corner = elf[2].split(',')
        if int(corner[0]) > left:
            left = int(corner[0])
        if int(corner[1][:-1]) > top:
            top = int(corner[1][:-1])
        dimensions = elf[3].split('x')
        if int(dimensions[0]) > width:
            width = int(dimensions[0])
        if int(dimensions[1]) > height:
            height = int(dimensions[1])
    return [left + width, top + height]                   


lines = getText('input.txt')
print(findUniqueElf(lines))
