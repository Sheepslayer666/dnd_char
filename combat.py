import utilites
import dice
import generator
import enemies

hit = None
is_combat = None

if dice.d20.roll() + generator.modifyer_set["strenght"]  > enemies.Goblin["AC"]:
    hit = True
else:
    hit = False
