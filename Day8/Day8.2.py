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
    """Compute the metadata at thie node"""
    #Next 2 values correspond to #immediate children, #metadata entires
    childs = tree[place]
    dataEntries = tree[place+1]
    place+=2

    #No children means get the metadata
    if childs == 0:
        for x in range(dataEntries):
            mData += tree[place]
            place += 1
        return mData, place

    #Yes children means sum the metadata of corresponding children
    childrenMDList = []

    #Recursively, compute child nodes' metadata, store into list
    while childs > 0:
        childrenData, nextNode = sumNode(0, place, tree)
        childrenMDList.append(childrenData)
        place = nextNode
        childs -= 1
        
    #After summing children, move on to summing the current metadata 
    while dataEntries > 0:
        if tree[place] <= len(childrenMDList) and tree[place] > 0:
            mData += childrenMDList[tree[place]-1]
        place += 1
        dataEntries -=1
    return mData, place


tree = getText('input.txt')
print(sumMetaData(tree))
