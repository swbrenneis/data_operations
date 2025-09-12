from random import randint

class Die:
    """ Class representing a single die """

    def __init__(self, num_sides=6):
        """ Assume a six sided die """
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)