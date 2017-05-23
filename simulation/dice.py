# This file defines the functionality of different Dice that will be used in the game.

class Dice:

    def __init__(self, sides):
        self.sides = sides
        self.num_successes = 0
        self.num_failures = 0
        self.successes = []
        self. failures = []

    def _assign_values(self):
        for i in range(self.sides):
            if i < self.num_successes:
                self.successes.append(i)
            else:
                self.failures.append(i)

    def set_values(self, successes, failures):
        assert successes + failures == self.sides, "ERROR: Number of successes and failures does not equal number of sides!!"
        self.num_successes = successes
        self.num_failures = failures
        self._assign_values()

    def roll(self):
        pass