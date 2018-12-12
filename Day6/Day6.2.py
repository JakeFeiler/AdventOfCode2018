#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import sys

def getText(text):
    f = open(text, 'r')
    lines = []
    for line in f:
        lines.append(line.strip().split(' '))
    f.close()
    return lines

#The most extreme coordinates
def getDimensions(lines):
    leftmost = int(lines[0][0][:-1])
    rightmost = int(lines[0][0][:-1])
    downmost = int(lines[0][1])
    upmost = int(lines[0][1])
    for line in lines:
        if int(line[0][:-1]) < leftmost:
            leftmost = int(line[0][:-1])
        if int(line[0][:-1]) > rightmost:
            rightmost = int(line[0][:-1])
        if int(line[1]) < downmost:                                           
            downmost = int(line[1])
        if int(line[1]) > upmost:                                                
            upmost = int(line[1])
    return (leftmost, rightmost, downmost, upmost)

#Given a square going from the most extreme points of the input:
#All possible points are within 200 (in this case) of the square
#Need within distance 10000, 50 lines of input, outside of 200 away,
#All are guaranteed to be at least 200 away -> total is bigger than 10000
def totalManhattan(lines, points):
    pointsSatisfied = 0
    for x in range(points[0]-int(10000/len(lines)),points[1]+int(10000/len(lines))+1):
        for y in range(points[2]-int(10000/len(lines)),points[3]+int(10000/len(lines))+1):
            distancesToPoint = 0
            for line in lines:
                point = (int(line[0][:-1]), int(line[1]))
                distancesToPoint += manhattan((x, y), point)
                if distancesToPoint >= 10000:
                    break
            if distancesToPoint < 10000:
                pointsSatisfied += 1
    return pointsSatisfied


def manhattan(p1, p2):                                                         
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

text = getText('input.txt')
points = getDimensions(text)
print(totalManhattan(text, points))
