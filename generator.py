import random
import utilites


random.shuffle(utilites.STANDARD_ARRAY)
skill_set_ply = {utilites.SKILLS[i]: utilites.STANDARD_ARRAY[i] for i in range(len(utilites.SKILLS))} 

spices_ply = input("Do you want to generate a human a dwarf or an elf?: ")
alligment_ply = input("Do you have an evil, good or neutral evil?: ")
porpuse = input("npc or villian?: ")


if alligment_ply == "good":
    random.shuffle(utilites.ALLIGNMENT_GOOD)
    selected_allignment = utilites.ALLIGNMENT_GOOD[0]
elif alligment_ply == "evil":
    random.shuffle(utilites.ALLIGNMENT_EVIL)
    selected_allignment = utilites.ALLIGNMENT_EVIL[0]
elif alligment_ply == "neutral":
    random.shuffle(utilites.ALLIGNMENT_NEUT)
    selected_allignment = utilites.ALLIGNMENT_NEUT[0]
else:
    print("Sorry this alligment is not supported")

def name_genrator():
    surename = str(random.choice(utilites.surenames_1)) + str(random.choice(utilites.surenames_2))
    if spices_ply == "human":
        givenname = random.choice(utilites.human_given_name)
    elif spices_ply == "elf":
        givenname = random.choice(utilites.elf_given_name)
    elif spices_ply == "dwarf":
        givenname = random.choice(utilites.dwarf_given_name)

    if alligment_ply == "evil":
        fullname = givenname + random.choice(utilites.evil_titles)
        print(fullname)
    elif alligment_ply == "neutral":
        fullname =givenname + " " + surename
        print(fullname)
    elif alligment_ply == "good":
        fullname = givenname + random.choice(utilites.good_titles)
        print(fullname)
    if alligment_ply == "evil":
        print(f"{fullname}" + " was feared")
    elif alligment_ply == "neutral":
        print(f"{fullname}" + " was okay, i mean okay notring special")
    elif alligment_ply == "neutral":
        print(f"{fullname}" + " was a wonderful person")
    return fullname


def backgroung_generator():
    flaw_ply = random.choice(utilites.FLAWS)
    bonds_ply = random.choice(utilites.BONDS)
    person_ply = random.sample(utilites.PERSONALITY_TRAIS, 2)
    print(selected_allignment)
    if "chaotic" in selected_allignment:
        ideals_ply = utilites.IDEALS.get("chaotic")
        print(ideals_ply)
    if "neutral" in selected_allignment:
        ideals_ply = utilites.IDEALS.get("neutral")
        print(ideals_ply)
    if "good" in selected_allignment:
        ideals_ply = utilites.IDEALS.get("good")
        print(ideals_ply)

name_genrator()
backgroung_generator()
print(skill_set_ply)

