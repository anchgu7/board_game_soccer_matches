# This file defines the functionality of different Dice that will be used in the game.

class Dice:

    def __init__(self, sides):
        self.sides = sides

    def set_sides(self, *args):
        pass

    def roll(self):
        pass


class D12(Dice):

    def __init__(self):
        Dice.__init__(12)
        self.num_of_offensive_successes = 0
        self.num_of_defensive_successes = 0
        self.num_of_blanks = 0
        self.offensive_successes = []
        self.defensive_successes = []
        self.blanks = []

    def _assign_values(self):
        total_successes = self.num_of_offensive_successes = self.num_of_defensive_successes
        for i in range(self.sides):
            if i < self.num_of_offensive_successes:
                self.offensive_successes.append(i)
            elif i > self.num_of_offensive_successes and i < total_successes:
                self.defensive_successes(i)
            else:
                self.blanks.append(i)

    def set_sides(self, num_of_offensive_successes, num_of_defensive_successes, num_of_blanks):
        assert num_of_offensive_successes + num_of_defensive_successes + num_of_blanks == self.sides

        self.num_of_offensive_successes = num_of_offensive_successes
        self.num_of_defensive_successes = num_of_defensive_successes
        self.num_of_blanks = num_of_blanks

        self._assign_values()

class D6(Dice):

    def __init__(self):
        Dice.__init__(6)