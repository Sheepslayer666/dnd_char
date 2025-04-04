import random
import utilites


random.shuffle(utilites.STANDARD_ARRAY)
skill_set_ply = {utilites.SKILLS[i]: utilites.STANDARD_ARRAY[i] for i in range(len(utilites.SKILLS))} 

spices_ply = input("Do you want to generate a human a dwarf or an elf?: ")
alligment_ply = input("Do you have an evil, good or neutral evil?: ")
porpuse = input("npc or villian?: ")


if alligment_ply == "good":
    random.shuffle(utilites.ALLIGNMENT_GOOD)
    print(utilites.ALLIGNMENT_GOOD[0])
elif alligment_ply == "evil":
    random.shuffle(utilites.ALLIGNMENT_EVIL)
    print(utilites.ALLIGNMENT_EVIL[0])
elif alligment_ply == "neutral":
    random.shuffle(utilites.ALLIGNMENT_NEUT)
    print(utilites.ALLIGNMENT_NEUT[0])
else:
    print("Sorry this alligment is not supported")

def name_genrator():
    if spices_ply == "human":
        givenname = random.choice(utilites.human_given_name)
        surename = str(random.choice(utilites.surenames_1)) + str(random.choice(utilites.surenames_2))
    elif spices_ply == "elf":
        givenname = random.choice(utilites.elf_given_name)
        surename = str(random.choice(utilites.surenames_1)) + str(random.choice(utilites.surenames_2))
    elif spices_ply == "dwarf":
        givenname = random.choice(utilites.dwarf_given_name)
        surename = str(random.choice(utilites.surenames_1)) + str(random.choice(utilites.surenames_2))

    if alligment_ply == "evil" or porpuse == "villian":
        fullname = givenname + " the worldeater"
        print(fullname)
    elif alligment_ply == "neutral" or porpuse == "npc":
        fullname =givenname + " " + surename
        print(fullname)
    elif alligment_ply == "good":
        fullname = givenname + " the heavenly"
        print(fullname)

fullname = name_genrator()

def backgroung_generator():
    if alligment_ply == "evil":
        print(f"{fullname}" + " was feared")
    elif alligment_ply == "neutral":
        print(f"{fullname}" + " was okay, i mean okay notring special")
    elif alligment_ply == "neutral":
        print(f"{fullname}" + " was a wonderful person")

name_genrator()
backgroung_generator()
print(skill_set_ply)

