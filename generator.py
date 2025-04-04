import random
import utilites


#Randomly schuffles the standard array and makes a dictionary with the skills
random.shuffle(utilites.STANDARD_ARRAY)
skill_set_ply = {utilites.SKILLS[i]: utilites.STANDARD_ARRAY[i] for i in range(len(utilites.SKILLS))} 

spices_ply = input("Do you want to generate a human a dwarf or an elf?: ")
alligment_ply = input("Do you have an evil, good or neutral evil?: ")
porpuse = input("npc or villian?: ")
"""spices_ply = "elf"
alligment_ply = "neutral"
porpuse = "npc"""

#Based on the good evil vlaies selects a random vlaue from the law chaos scale
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
    #Takes a radnom name based on the spices and makes a random surename indifferent for the spices
    surename = str(random.choice(utilites.surenames_1)) + str(random.choice(utilites.surenames_2))
    if spices_ply == "human":
        givenname = random.choice(utilites.human_given_name)
    elif spices_ply == "elf":
        givenname = random.choice(utilites.elf_given_name)
    elif spices_ply == "dwarf":
        givenname = random.choice(utilites.dwarf_given_name)
    #Assignes a title or surename based on the allignment
    if alligment_ply == "evil":
        fullname = givenname + random.choice(utilites.evil_titles)
        print(fullname)
    elif alligment_ply == "neutral":
        fullname =givenname + " " + surename
        print(fullname)
    elif alligment_ply == "good":
        fullname = givenname + random.choice(utilites.good_titles)
        print(fullname)
    #Gives a short description of the NPC based on allignments
    #TODO have be moved for the background generation
    if alligment_ply == "evil":
        print(f"{fullname}" + " was feared")
    elif alligment_ply == "neutral":
        print(f"{fullname}" + " was okay, i mean okay notring special")
    elif alligment_ply == "neutral":
        print(f"{fullname}" + " was a wonderful person")
    return fullname


def backgroung_generator():
    #Generates randomised backgorund
    flaw_ply = random.choice(utilites.FLAWS)
    bonds_ply = random.choice(utilites.BONDS)
    person_ply = random.sample(utilites.PERSONALITY_TRAIS, 2)
    general_ideal1 = utilites.IDEALS.get("all1")
    general_ideal2 = utilites.IDEALS.get("all2")
    ideal_list = []
    ideal_list.append(utilites.IDEALS.get("all1"))
    ideal_list.append(utilites.IDEALS.get("all2"))
    print(selected_allignment)
    #Selects one allignment convinient ideal
    if "chaotic" in selected_allignment:
        ideal_list.append(utilites.IDEALS.get("chaotic"))
        ideal_ply = random.choice(ideal_list)
        print(ideal_ply)
    if "neutral" in selected_allignment:
        ideal_list.append(utilites.IDEALS.get("neutral"))
        ideal_ply = random.choice(ideal_list)
        print(ideal_ply)
    if "good" in selected_allignment:
        ideal_list.append(utilites.IDEALS.get("good"))
        ideal_ply = random.choice(ideal_list)
        print(ideal_ply)

name_genrator()
backgroung_generator()
print(skill_set_ply)

