#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import sys

def sumInput(text):
    f =  open(text, 'r')
    sum = 0
    count = 1
    for line in f:
        count += 1
        line = line.strip()
        if (line[0] == '+'):
            sum += int(line[1:])
        else:
            sum -= int(line[1:])
    f.close()
    return sum

def main():
    print(sumInput('input.txt'))

if __name__ == "__main__":
    main()
