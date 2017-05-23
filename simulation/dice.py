# This file defines the functionality of different Dice that will be used in the game.

class Dice:

    def __init__(self, sides):
        self.sides = sides
        self.successes = 0
        self.failures = 0

    def set_values(self, successes, failures):
        assert successes + failures == self.sides, "ERROR: Number of successes and failures does not equal number of sides!!"
        self.successes = successes
        self.failures = failures

    def roll(self):
        pass