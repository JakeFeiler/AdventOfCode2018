#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import sys
import re
import matplotlib.pyplot as plt


def get_text(text):
    f = open(text, 'r')
    lines = []
    raw_lines = [re.split(r'<(.*?)>',line.strip()) for line in f]
    for raw_line in raw_lines:
        lines.append((raw_line[1].split(', '), raw_line[3].split(', ')))
    return lines

def print_picture(lines):
    """Print out the images as time progresses"""
    coords, velocities = zip(*lines)
    coords = [tuple(map(int, c)) for c in coords]
    velocities = [tuple(map(int, v)) for v in velocities]

    #Input inspection: 10500 seconds would leave most coordinates about |500| from origin
    for z in range(10500, 10600):
        updated_coords = [(x + v1*z, y + v2*z) for (x, y), (v1, v2) in zip(coords, velocities)]
        x,y = zip(*updated_coords)

        #Using matplot to graph points
        fig = plt.scatter(x,y)

        #To more confortably read the message, set the window size and flip over the y-axis
        plt.rcParams["figure.figsize"] = (12,3)
        plt.gca().invert_yaxis()
        title = "Seconds passed: " + str(z)
        plt.title(title)
        plt.show()
        #Inputting allows to continue with sequence of images
        input("Press ENTER to continue")
        plt.close()

def main():
    lines = get_text('input.txt')

    #Ion enables program to continue after plt.show()
    plt.ion()
    print_picture(lines)


if __name__ == '__main__':
    main()
