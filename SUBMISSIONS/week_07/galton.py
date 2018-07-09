""" Allow the user to setup and play with a Galton's Box """

import random

class Marble:
    """ Represent a marble that will be dropped through the Galton's Box """

    def __init__(self, name):
        self.name = name
        self.position = None       

class GaltonBox:
    """ Represent the overall setup of the game """

    def __init__(self, rows):
        self.marbles = []
        self.rows = rows
    
    def insert_marble(self, marble):
        self.marbles.append(marble)
        marble.position = (0, 0)

    def time_step(self):
        for marble in self.marbles:
            if random.choice(['Left', 'Right']) is 'Left':
                marble.position[1] += 1
            else:
                marble.position[0] += 1 
                marble.position[1] += 1

    def __str__(self):
        box_status = []
        marbles_positions = [marble for marble in self.marbles]
        setup = []
        for r in range(1, self.rows):
            setup.append('-' * r)

            for c in range(self.marbles):
                if (r, c) in :
                    box_row.append(c.name())
                else:
                    box_row.append('-')
            box_status.append(box_row)
        return box_status