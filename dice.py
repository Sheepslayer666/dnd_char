#Dice set\
import random

class dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1,self.sides)
d2 = dice(2)
d3 = dice(3)
d4 = dice(4)
d6 = dice(6)
d8 = dice(8)
d12 = dice(12)
d20 = dice(20)