# This file defines the various types of Players that can be playing in a Game. Each Player is different based on their
# Position, however each Player also has similarities. Therefore, each Individual Player inherits from the base Player
# class.

# Author: Andrew Guerra
from dice import Dice

class Player:

    def __init__(self):
        # Each Player has the following member variables:
        # 1. A "D12" (Dice Object) that is rolled for its action.
        # 2. The "number of rolls" (int) the Player can roll each time they have to roll.
        # 3. Three booleans, that are results of rolling the Reckless Die.
        #       1. "Injured" --> the Player becomes injured
        #       2. "Ejected" --> the Player gets a Red Card
        #       3. "Warned" --> the Player gets a Yellow Card
        self.D12 = Dice(12)
        self.number_of_rolls = 1
        self.injured = False
        self.ejected = False
        self.warned = False

    def offensive_play(self):
        # This method is overridden in each subclass. It defines what the Player does when it's making a roll while
        # on Offense.
        pass

    def defensive_play(self):
        # This method is overridden in each subclass. It defines what the Player does when it's making a roll while
        # on Defense.
        pass


class Keeper(Player):

    def __init__(self):
        Player.__init__()


    def offensive_play(self):
        pass

    def defensive_play(self):
        pass


class Defender(Player):

    def offensive_play(self):
        pass

    def defensive_play(self):
        pass


class Midfielder(Player):

    def offensive_play(self):
        pass

    def defensive_play(self):
        pass


class Forward(Player):

    def offensive_play(self):
        pass

    def defensive_play(self):
        pass
