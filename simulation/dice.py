# This file defines the functionality of different Dice that will be used in the game.

class Dice:

    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        pass


class D12(Dice):

    def __init__(self):
        Dice.__init__(12)


class D6(Dice):

    def __init__(self):
        Dice.__init__(6)