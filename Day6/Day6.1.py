#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3


import sys
import numpy

def getText(text):
    f = open(text, 'r')
    return [line.strip().split(' ') for line in f]

#Get the rightmost and downmost coordinate from the input
#Can form a grid, all points on the edge correspond to infinite areas
def getDimensions(lines):
    rightmost = 0
    downmost = 0
    for line in lines:
        if int(line[0][:-1]) > rightmost:
            rightmost = int(line[0][:-1])
        if int(line[1]) > downmost:
            downmost = int(line[1])
    return downmost, rightmost

def getBiggestArea(lines, dims):
    #Set up grid
    
    grid = [[0] * (1 + dims[1]) for k in range(1 + dims[0])]
    #Set up list to track areas covered by each point
    areaOfPoint = [0]*len(lines)
    #On every point in the grid, compute manhattan distance to every point in inpu
    #Set grid value equal to the input number
    for i, row in enumerate(grid):
        for j, col in enumerate(grid[i]):
            closest = -1
            distance = dims[0] + dims[1]
            for l, line in enumerate(lines):
                xCoord = int(line[0][:-1])
                yCoord = int(line[1])
                d = manhattan((i, j), (xCoord, yCoord))
                if d < distance:
                    distance = d
                    closest = l
                #Tie means no value
                elif d == distance:
                    closest = -1
            grid[i][j] = closest

    for i in range(dims[0]):
           for j in range(dims[1]):
               print(grid[i][j])

    #Get total areas of points in interior (edge doesn't matter)
    for x in range (1, dims[0]):
        for y in range(1, dims[0]):
            if grid[x][y] != 1:
                areaOfPoint[grid[x][y]] += 1

    #Edge values correspond to infinite areas
    for a in range(dims[0]):
        if grid[a][0] != -1:
            areaOfPoint[grid[a][0]] = 0
        if grid[a][dims[1]] != -1:
            areaOfPoint[grid[a][dims[1]]] = 0
    for b in range(dims[1]):
        if grid[0][b] != -1:
            areaOfPoint[grid[0][b]] = 0
        if grid[dims[0]][b] != -1:
            areaOfPoint[grid[dims[0]][b]] = 0

    return max(areaOfPoint)
    

def manhattan(p1, p2):
 #   print(p1, p2)
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def main():
    lines = getText('input.txt')
    dimensions = (getDimensions(lines))
    print(getBiggestArea(lines, dimensions))

if __name__ == "__main__":
    main()
