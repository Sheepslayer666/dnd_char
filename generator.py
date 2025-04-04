import random


STANDARD_ARRAY = [15, 14, 13, 12, 10, 8]
ALLIGNMENT_GOOD = ["Lawful good", "Neutral good", "Chaotic good"]
ALLIGNMENT_EVIL = ["Lawful neutral", "True Neutral", "Chaotic neutral"]
ALLIGNMENT_NEUT = ["Lawful evil", "Neutral evil", "Neutral evil"]
SKILLS = ["strenght", "dexterity", "intelligence", "wisdom", "charisma"]
SPECIES = ["Dwarf", "Elf", "Halfling", "Human"]
human_given_name = ["Frederic", "Goldwyn", "Bob", "Billard", "Rudolf", "Bloodwyn", "Gomez"]
dwarf_given_name = ["Olin", "Brewin", "Dalin", "Thorin", "Thorlof", "Arnulf"]
elf_given_name = ["Dalion", "Tylion", "Quillion", "Cyndrion"]
surenames_1 = ["Iron", "Horse", "Tree", "Beer", "Wolf", "Bow", "Light", "Fire", "Oak"]
surenames_2 = ["master", "caster", "killer", "foe", "hand", "frined", "traveller"]


random.shuffle(STANDARD_ARRAY)
skill_set_ply = {SKILLS[i]: STANDARD_ARRAY[i] for i in range(len(SKILLS))} 

spices_ply = input("Do you want to generate a human a dwarf or an elf?: ")
alligment_ply = input("Do you have an evil, good or neutral evil?: ")
porpuse = input("npc or villian?: ")

if alligment_ply == "good":
    random.shuffle(ALLIGNMENT_GOOD)
    print(ALLIGNMENT_GOOD[0])
elif alligment_ply == "evil":
    random.shuffle(ALLIGNMENT_EVIL)
    print(ALLIGNMENT_EVIL[0])
elif alligment_ply == "neutral":
    random.shuffle(ALLIGNMENT_NEUT)
    print(ALLIGNMENT_NEUT[0])
else:
    print("Sorry this alligment is not supported")

def name_genrator():
    if spices_ply == "human":
        givenname = random.choice(human_given_name)
        surename = str(random.choice(surenames_1)) + str(random.choice(surenames_2))
    elif spices_ply == "elf":
        givenname = random.choice(elf_given_name)
        surename = str(random.choice(surenames_1)) + str(random.choice(surenames_2))
    elif spices_ply == "dwarf":
        givenname = random.choice(dwarf_given_name)
        surename = str(random.choice(surenames_1)) + str(random.choice(surenames_2))

    if alligment_ply == "evil" or porpuse == "villian":
        fullname = givenname + " the worldeater"
        print(fullname)
    elif alligment_ply == "neutral" or porpuse == "npc":
        fullname =givenname + " " + surename
        print(fullname)
    elif alligment_ply == "good":
        fullname = givenname + " the heavenly"
        print(fullname)

name_genrator()
print(skill_set_ply)

