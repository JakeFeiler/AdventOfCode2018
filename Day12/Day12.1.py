#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import sys
import re

def get_text(text):
    lines = []
    initial_state = ''
    with open(text, 'r') as f:
        initial_state = f.readline().strip()[15:]
        for line in f:
            if not re.match(r'^\s*$', line):
                lines.append(line.rstrip().split(' => '))
        return initial_state, lines


def compute_generations(initial_state, lines, iters):
    """Determine the resulting configuration after 20 generations"""
    #Convert the input into a dictionary
    spread_patterns = dict(lines)
    initial_length = len(initial_state)

    #Note that a plant can certainly spread by no more than 2 from an existing plant
    #For this new plant 2 away, we need to know the plants 2 away from that
    #So extra_pots=42 on either side is sufficient for 20 generations
    extra_pots = 2 + iters*2
    configuration = '.'*extra_pots + initial_state + '.'*extra_pots
    #Note that '.....' => '.', so we don't need to search too far immediately
    for generation in range(iters):
        print(generation, sum_pots(configuration, extra_pots))
        #Every generation, check the status of possibly affected pots, and update the configuration
        new_state = ''
        for pot in range(-2 - generation*2, initial_length + 2 + 2*generation):
            new_state += spread_patterns[configuration[extra_pots - 2 + pot:extra_pots + 3 + pot]]
        configuration = '.'*(extra_pots - 2*(generation + 1)) + new_state + '.'*(extra_pots - 2*(generation + 1))

    return sum_pots(configuration, extra_pots)


def sum_pots(configuration, extra_pots):
    """Given a configuration, find the sum of the pots with plants in them (middle pot is 0)"""
    sum_of_plants = 0
    for index, plant in enumerate(configuration):
        if plant == '#':
            sum_of_plants += index - extra_pots

    return sum_of_plants


def main():
    initial_state, lines = get_text('input.txt')
    generations = 1000
    print(compute_generations(initial_state, lines, generations))

if __name__ == "__main__":
    main()
