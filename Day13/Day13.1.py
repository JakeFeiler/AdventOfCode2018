#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import operator

#Note: spec lists x-coordinate as the column, y-coordinate at the row
#At the end, need to flip my coordinates since I did it backwards

def get_text(text):
    carts = []
    with open(text, 'r') as f:
        lines = f.readlines()
    path = []
    for row_index, line in enumerate(lines):
        path_row = []
        #If cart detected, replace with correct track direction in the map
        for column_index, character in enumerate(line):
            if character == 'v':
                carts.append(Cart('D', row_index, column_index))
                path_row.append('|')
            elif character == '^':
                carts.append(Cart('U', row_index, column_index))
                path_row.append('|')
            elif character == '>':
                carts.append(Cart('R', row_index, column_index))
                path_row.append('-')
            elif character == '<':
                carts.append(Cart('L', row_index, column_index))
                path_row.append('_')
            else:
                path_row.append(character)
        path.append(path_row)
    return carts, path

class Cart:
    '''Cart objects that will be patrolling the railroads'''
    def __init__(self, d, x, y):
        '''Initialize a cart object'''
        self.direction = d
        self.intersections = 0
        self.coords = (x, y)

    def move(self):
        '''Move the cart in the correct direction'''
        if self.direction == 'U':
            self.coords = tuple(map(operator.add, self.coords, (-1, 0)))
        elif self.direction == 'D':
            self.coords = tuple(map(operator.add, self.coords, (1, 0)))
        elif self.direction == 'L':
            self.coords = tuple(map(operator.add, self.coords, (0, -1)))
        elif self.direction == 'R':
            self.coords = tuple(map(operator.add, self.coords, (0, 1)))

    def set_direction(self, track):
        '''Set the new cart direction depending on its location, and check for collision'''
        if track in ['|', '-']:
            pass
        #Turn guide dictionary determines new direction based on old direction
        elif track == '\\':
            turn_guide = {'U': 'L', 'L': 'U', 'D': 'R', 'R': 'D'}
            self.direction = turn_guide[self.direction]
        elif track == '/':
            turn_guide = {'U': 'R', 'R': 'U', 'D': 'L', 'L': 'D'}
            self.direction = turn_guide[self.direction]
        elif track == '+':
            self.intersections += 1
            if self.intersections % 3 == 1:
                #Turn left
                turn_guide = {'U': 'L', 'L': 'D', 'D': 'R', 'R': 'U'}
                self.direction = turn_guide[self.direction]
            elif self.intersections % 3 == 0:
                #Turn right
                turn_guide = {'U': 'R', 'R': 'D', 'D': 'L', 'L': 'U'}
                self.direction = turn_guide[self.direction]
            else:
                #Intersection % 3 == 2 => stay straight
                pass

def run_carts(carts, paths):
    '''Run the carts until a collision happens'''
    coords = (0, 0)
    have_not_collided = True
    ticks = 0
    while have_not_collided:
        ticks += 1

        #Sort the carts by coordinates to advance in the correct order
        carts.sort(key=lambda cart: (cart.coords[0], cart.coords[1]))
        for moving_cart in carts:
            moving_cart.move()
            track = paths[moving_cart.coords[0]][moving_cart.coords[1]]
            moving_cart.set_direction(track)

            #Find the number of carts sharing the same position, including the same cart
            #Would therefore need 2 carts for a collision to happen
            overlap = 0
            for other_cart in carts:
                if moving_cart.coords == other_cart.coords:
                    overlap += 1

            if overlap > 1:
                have_not_collided = False
                #Here is the reverse
                coords = (moving_cart.coords[1], moving_cart.coords[0])
                break
    return coords

carts, CART_PATHS = get_text('input.txt')
print(run_carts(carts, CART_PATHS))
