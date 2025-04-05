import utilites
import dice
import generator

hit = None

if dice.d20.roll() + generator.modifyer_set["strenght"]  > utilites.Enemies["Goblin"]:
    hit = True
else:
    hit = False
