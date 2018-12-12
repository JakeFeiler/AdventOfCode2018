#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys
import string

def getText(inputText):
    text = open(inputText,'r')
    lines = [line.strip().split(' ') for line in text]
    return lines



def getOrder(text):
    """Create an array tracking the immediate dependencies for every letter"""
    """Loop through while there still exist dependencies, do the first element with no dependencies left"""
    dependencies = ['']*26
    finalOrder = ''
    alphaDict = {k: v for  v, k in enumerate(string.ascii_uppercase)}
    
    #Value v at position p in dependencies: steps v to be completed before p
    for line in text:
        dependencies[alphaDict[line[7]]] += line[1]

    initialDependencies = dependencies.copy() 
    
    #26 iterations sufficient to find order, remove 'no dependencies', update rest accordingly
    for x in range(26):
        for value, dependency in enumerate(dependencies):
            if dependency == '':
                finalOrder += string.ascii_uppercase[value]
                dependencies[value] = '0'
                #Remove all instances of the corresponding letter from all dependencies
                for y in range(26):
                    dependencies[y] = dependencies[y].replace(string.ascii_uppercase[value], '')
                break
            
    return (finalOrder, initialDependencies)

def getTotalTime(order, dependencies):
    minutes = 0
    minutesRemaining = [60]*26
    alphaDict = {k: v for  v, k in enumerate(string.ascii_uppercase)}
    for x in range(26):
        minutesRemaining[x] += (x+1)

    #Brute force: run an iteration every minute, will decrease up to 5 tasks
    while (max(minutesRemaining) != 0):
        minutes += 1
        workers = 5
        simultaneousWorkings = []

        #order =, i.e, BFLXWHPOMA....
        for toDo in order:
           #If no workers free, move to next minute
           if workers <= 0:
               break
           if minutesRemaining[alphaDict[toDo]] > 0 and dependencies[alphaDict[toDo]] == '':
               simultaneousWorkings.append(toDo)
               workers  -= 1

        #Originally had below block in for loop
        #However, need to make sure all jobs are done simultaneously so that job A doesn't finish allowing job B to start a minute early
        for task in simultaneousWorkings:
            minutesRemaining[alphaDict[task]] -= 1
            #If task is complete, adjust the corresponding dependencies
            if minutesRemaining[alphaDict[task]] == 0:
                for y in range(26):
                    dependencies[y] = dependencies[y].replace(task, '')
    
    return minutes

def main():
    lines = getText('input.txt')
    order, dependencies = getOrder(lines)
    print(getTotalTime(order, dependencies))

if __name__== "__main__":
    main()

#Note for this problem: fortunately, the 60 minute baseline for a task + 5 alloted workers
#assures us optimization with this method. However, given smaller times for tasks and/or fewer workers
#this won't necessarily be effective
