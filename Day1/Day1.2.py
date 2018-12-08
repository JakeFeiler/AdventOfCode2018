#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

def findDuplicateFrequency(text):
    f =  open(text, 'r')
    total = 0
    changes = createFreqLoop(text)
    frequencies = []
    return loopList(total, changes, frequencies)


#Create a list containing all the frequency changes
def createFreqLoop(text):
    f = open(text, 'r')
    changes = []
    for line in f:
        line = line.strip()
        if (line[0] == '+'):
            changes.append(int(line[1:]))
        else:
            changes.append(int(line[1:]) * -1)
    return changes

#Maintain list of past frequencies, freqs, add changes until duplicate discovered
def loopList(t, changes, freqs):
    for change in changes:
        t += change
        for freq in freqs:
            if (t == freq):
                return t
        freqs.append(t)
    return loopList(t,changes,freqs)


print('Patience...')
print(findDuplicateFrequency('input.txt'))
#print(createFreqLoop('input.txt'))
