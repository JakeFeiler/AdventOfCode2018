#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3                 
                                                                                
import sys
from operator import itemgetter

def getText(text):
    times = []
    f = open(text, 'r')
    for line in f:
        times.append(line.strip().split())
    #Sort the data by first 2 words (the date/time)
    return sorted(times, key=itemgetter(0,1))


def findSleepyGuard(times):
    #Dictionary List
    naps = {}
    guardNum = 0
    sleepStart = 0
    sleepEnd = 0
    sleepTime = 0
    for i in times:
        #Update dictionary by adding current guard's sleep time, then update the guard number 
        if i[3][0] == '#':
            if guardNum > 0:
                #Update dictionary info for guard naptime
                if guardNum in naps:
                    naps[guardNum] += sleepTime
                else:
                    naps[guardNum] = sleepTime
            guardNum = int(i[3][1:])
            sleepStart = 0
            sleepEnd = 0
            sleepTime = 0
        if i[2] == 'falls':
            sleepStart = int(i[1][-3:-1])
        if i[2] == 'wakes':
            sleepEnd = int(i[1][-3:-1])
            sleepTime += sleepEnd - sleepStart
            sleepStart = 0
            sleepEnd = 0
    #return guard who sleeps the most
    return max(naps, key=naps.get)

def findSleepMinute(guard, times):
    minutes = [0]*60
    sleepStart = 0
    sleepEnd = 0
    rightGuard = False
    for i in times:
        #Wait for the right guard to appear, then start incrementing the minutes he sleeps
        if i[3][0] == '#':
            if int(i[3][1:]) == guard:
                rightGuard = True
            else:
                rightGuard = False
        if rightGuard == True:
            if i[2] == 'falls':
                sleepStart = int(i[1][-3:-1])
            elif i[2] == 'wakes':
                sleepEnd = int(i[1][-3:-1])
                #Guard woke up, now know every minute they just slept
                for j in range(sleepStart, sleepEnd):
                    minutes[j] += 1
                    sleepStart = 0
                    sleepEnd = 0
    return minutes.index(max(minutes))
  
times = getText('input.txt')
guard = findSleepyGuard(times)
minute = findSleepMinute(guard,times)
print(guard*minute)

