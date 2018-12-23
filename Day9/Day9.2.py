#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import sys
import collections

#After poor choice to implement list for part 1:
#Using a deque for part 2 (double end queue, works like list)

def findWinner(marbles, players):
    scores = [0]*players
    center = collections.deque([0])
    player = 1
    for m in range(1,marbles+1):
        if m % 23 == 0:
            scores[player] += m
            center.rotate(7)
            scores[player] += center.pop()
            center.rotate(-1)
        else:
            center.rotate(-1)
            center.append(m)
        player = (player + 1) % players
    return max(scores)
    

print(findWinner(71058*100,411))
