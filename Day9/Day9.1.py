#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import sys

def findWinner(marbles, players):
    scores = [0]*players
    center = [0]
    position = 1
    player = 1
    for m in range(1,marbles+1):
        if m % 23 == 0:
            scores[player] += m
            position = (position - 7) % len(center)
            scores[player] += center[position]
            center.pop(position)
        else:
            position = position + 2
            if position > len(center):
                position = 1
            center.insert(position,m)
        player = (player + 1) % players
    return max(scores)
    
print(findWinner(71058, 411))
