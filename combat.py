import dice
import generator
import enemies

hit = None
is_combat = False

while is_combat == True:
    if dice.d20.roll() + generator.modifyer_set["strenght"]  > enemies.Goblin["AC"]:
        hit = True
    else:
        hit = False
