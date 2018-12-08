#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import sys

def getText(text):
    ids = []
    f = open(text, 'r')
    for line in f:
        f = line.strip()
        ids.append(line.split()[2:])
    return ids

def countOverlap(lines):
    overlappedSquares = 0
    dims = maxSize(lines)
    #Fabric is matrix, will count usage of every squrae
    fabric = [0]*dims[0]
    for i in range(dims[0]):
        fabric[i] = [0]*dims[1]
    for elf in lines:
        corner = elf[0].split(',')
        left = int(corner[0])
        top = int(corner[1][:-1])
        dimensions = elf[1].split('x')
        #For every elf, increment the values of 'fabric' corresponding to the square they use
        for i in range(0, int(dimensions[0])):
            for j in range(0, int(dimensions[1])):
                fabric[left + i][top + j] +=1
                if fabric[left + i][top + j] == 2:
                    #Shared squares increases once a value of fabric reaches 2
                    overlappedSquares += 1
    return overlappedSquares


#Going to create a matrix of all squares, need to set size by finding the biggest possble dimensions
#Height: Lowest possible coordinate + largest possible square height
#Width: Right-est possible coordinate + largest posibile square width
def maxSize(lines):
    left  = 0
    top = 0
    width = 0
    height = 0
    for elf in lines:
        corner = elf[0].split(',')
        if int(corner[0]) > left:
            left = int(corner[0])
        if int(corner[1][:-1]) > top:
            top = int(corner[1][:-1])
        dimensions = elf[1].split('x')
        if int(dimensions[0]) > width:
            width = int(dimensions[0])
        if int(dimensions[1]) > height:
            height = int(dimensions[1])
    return [left + width, top + height]                   


lines = getText('input.txt')
print(countOverlap(lines))
