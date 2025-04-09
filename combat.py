import dice
#import generator
import enemies
import player
import math

hit = None
is_combat = False
position_ply = [1]
postion_enemy = [0]

while math.dist(position_ply, postion_enemy) <= 10.0:
    is_combat = True


while is_combat == True:
    if dice.d20.roll() + generator.modifyer_set["strenght"]  > enemies.Goblin["AC"]:
        hit = True
    else:
        hit = False