import dice
import generator
import enemies
import player
import math

hit = None
is_combat = False
position_ply = [1]
postion_enemy = [0]
distance = math.dist(position_ply, postion_enemy)

while distance <= 10.0:
    is_combat is True

while is_combat == True:
    if dice.d20.roll() + generator.modifyer_set["strenght"]  > enemies.Goblin["AC"]:
        hit = True
    else:
        hit = False