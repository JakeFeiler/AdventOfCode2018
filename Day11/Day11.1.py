#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import sys
import numpy as np

def compute_power_levels(serial_number):
    """Find the power level of every square in the grid, then return largest 3x3 total"""
    fuel_cells = [[0]*300 for i in range(300)]

    for x in range(300):
        for y in range(300):
            #Remember: Lists indexed beginning at 0, but spec begins at 1
            rack_ID = x + 11
            power_level = rack_ID*(y+1)
            power_level += serial_number
            power_level *= rack_ID
            power_level = int(power_level/100)%10 - 5
            fuel_cells[x][y] = power_level

    #Could do brute force computation from here
    #But to prevent some redundant addition, we can first store every sum of 3 consecutive row cells
    row_cells = [[0]*298 for j in range(300)]
    for r in range(300):
        for c in range(298):
            row_cells[r][c] = fuel_cells[r][c] + fuel_cells[r][c+1] + fuel_cells[r][c+2]

    #And then store the sums of 3 consecutive column cells from the previous grid
    #Not easy to use shortcut to find the index of the maximum, so doing it by force
    max_value = 9*(-5)
    coords = (0, 0)
    for r2 in range(298):
        for c2 in range(298):
            value = row_cells[r2][c2] + row_cells[r2+1][c2] + row_cells[r2+2][c2]
            if value > max_value:
                max_value = value
                coords = (r2+1, c2+1)
    return coords

INPUT = 7689
print(compute_power_levels(INPUT))
