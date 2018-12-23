#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import sys

def getText(text):
    f  = open(text, 'r')
    tree = f.read().strip().split(' ')
    return list(map(int, tree))

def sumMetaData(tree):
    metaData, placeholder = sumNode(0,0,tree)
    return metaData

def sumNode(mData, place, tree):
    """sum the metadata beginning at position place in the tree of values"""
    #Next 2 values correspond to #immediate children, #metadata entires
    childs = tree[place]
    dataEntries = tree[place+1]
    place += 2

    #Recursively, sum the child nodes
    while childs > 0:
        childrenData, nextNode = sumNode(0, place, tree)
        mData += childrenData
        place = nextNode
        childs -= 1
        
    #After summing children, move on to summing the current metadata 
    while dataEntries > 0:
        mData += tree[place]
        place += 1
        dataEntries -=1
    return mData, place


tree = getText('input.txt')
print(sumMetaData(tree))
