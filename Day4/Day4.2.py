#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import sys
from operator import itemgetter

def getText(text):                  
    times = []         
    f = open(text, 'r')              
    for line in f:
        times.append(line.strip().split())                                     
    return sorted(times, key=itemgetter(0,1))

def findBestMinute(times):
    #naps is now a dictionary with the values being lists of size 60 for every guard's minutes
    naps = {}
    guardNum = 0
    sleepStart = 0
    sleepEnd = 0
    for i in times:
        if i[3][0] == '#':
            guardNum = int(i[3][1:])
        if i[2] == 'falls':
            sleepStart = int(i[1][-3:-1])
        if i[2] == 'wakes':
            sleepEnd = int(i[1][-3:-1])
            if guardNum not in naps:
                naps[guardNum] = [0]*60
            for x in range(sleepStart,sleepEnd):
                naps[guardNum][x] += 1
            sleepStart = 0
            sleepEnd = 0

    mostMinutes = 0
    minuteNum = 0
    guardNumber = 0
    #Find the greatest value in a list in the dictionary
    for guard in naps:
        for minute, minutesSlept in enumerate(naps[guard]):
            if minutesSlept > mostMinutes:
                mostMinutes = minutesSlept
                minuteNum = minute
                guardNum = guard
    return guardNum * minuteNum

times = getText('input.txt')
print(findBestMinute(times))
