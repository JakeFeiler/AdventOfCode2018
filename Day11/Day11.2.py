#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

def compute_power_levels(serial_number):
    """Find the power level of every square in the grid, then return largest square total"""
    coords = (0, 0, 0)
    max_power = 0
    #3-dimensional matrix, to mark the power level at every square for all possible sizes
    #fuel_cells[x][y][z]: square of (z+1)^2 size starting at (x+1,y+1)
    fuel_cells = [[[0]*300 for a in range(300)] for b in range(300)]

    for x in range(300):
        for y in range(300):
            #Remember: Lists indexed beginning at 0, but spec begins at 1
            rack_ID = x + 11
            power_level = rack_ID*(y+1)
            power_level += serial_number
            power_level *= rack_ID
            power_level = int(power_level/100)%10 - 5
            fuel_cells[x][y][0] = power_level
            if power_level > max_power:
                max_power = power_level
                coords = (x+1, y+1, 1)

    #To quickly calculate power level of any size at any point in the grid
    #Use [x][y][z] = [x+1][y][z-1] + [x][y+1][z-1] - [x+1][y+1][z-2] + [x+z][y+z][0] + [x][y][0]
    #In other words: add 1-smaller square of coordinate directly below and right
    #Then subtract 2-smaller square of direct below-right
    #Then add the bottom right and the new top left values of the square

    for square_size in range(1, 300):
        for row in range(300 - square_size):
            for col in range(300 - square_size):
                power_level = fuel_cells[row][col][0] + fuel_cells[row + 1][col][square_size - 1] + fuel_cells[row][col + 1][square_size - 1]
                if square_size > 1:
                    power_level -= fuel_cells[row + 1][col + 1][square_size - 2]
                power_level += fuel_cells[row + square_size][col + square_size][0]
                fuel_cells[row][col][square_size] = power_level
                if power_level > max_power:
                    max_power = power_level
                    coords = (row + 1, col + 1, square_size + 1)


    return coords





INPUT = 7689
print(compute_power_levels(INPUT))
