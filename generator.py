import random
import utilites
import dice

#Randomly schuffles the standard array and makes a dictionary with the skills
random.shuffle(utilites.STANDARD_ARRAY)
skill_set_ply = {}

spices_ply = input("Do you want to generate a human a dwarf a halfling or an elf?: ")
while spices_ply.lower() not in utilites.SPECIES:
    spices_ply = input("Do you want to generate a human a dwarf a halfling or an elf?: ")

alligment_ply = input("Do you want to have a good, neutral, evil or random NPC?: ")
while alligment_ply not in utilites.BASE_ALLGINMENT and alligment_ply != "random":
    alligment_ply = input("Do you want to have a good, neutral, evil or random NPC?: ")

class_ply = input("What class do you want?: ")
while class_ply.lower() not in utilites.CLASSES and class_ply != "random":
    class_ply = input("What class do you wan?: ")

name_ply = input("Do you want a name or wanto generate randomly? ")
if name_ply != "random":
    answer = input(f"Are you sure you wanf to name your character: {name_ply} yes or no?")
    if answer.lower() == "no":
        name_ply = input("Do you want a name or wanto generate randomly? ")

porpuse = input("npc or villian?: ")
while porpuse.lower() not in utilites.PORPOUSE:
    porpuse = input("npc or villian?: ")
#support to modes of creating a character random rolls by dice or SA
mode = input("What modes you want to generate the NPC, sa (standard array) or dice?: ")
while mode.lower() not in utilites.MODES:
    mode = input("What modes you want to generate the NPC, sa (standard array) or dice?: ")


if class_ply == "random":
    class_ply = random.choice(utilites.CLASSES)

if mode == "sa":
    skill_set_ply = {utilites.SKILLS[i]: utilites.STANDARD_ARRAY[i] for i in range(len(utilites.SKILLS))}

elif mode == "dice":
    skill_set_ply = {utilites.SKILLS[i]: dice.dice(20).roll() for i in range(len(utilites.SKILLS))}


modifyer_set = skill_set_ply.copy()
summary_ply = None
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
elif alligment_ply == "random":
    base = random.choice(utilites.BASE_ALLGINMENT)
    if base == "neutral":
        selected_allignment = "True " + base
    else:
        selected_allignment = random.choice(["Lawful ", "Chaotic "]) + base
else:
    print("Sorry this alligment is not supported")

if alligment_ply == "random":
    if "neutral" in selected_allignment:
        alligment_ply = "neutral"
    elif "evil" in selected_allignment:
        alligment_ply = "evil"
    elif "good" in selected_allignment:
        alligment_ply = "good"

def name_genrator():
    #Takes a radnom name based on the spices and makes a random surename indifferent for the spices
    surename = str(random.choice(utilites.surenames_1)) + str(random.choice(utilites.surenames_2))
    if spices_ply == "human":
        givenname = random.choice(utilites.human_given_name)
    elif spices_ply == "elf":
        givenname = random.choice(utilites.elf_given_name)
    elif spices_ply == "dwarf":
        givenname = random.choice(utilites.dwarf_given_name)
    elif spices_ply == "halfling":
        givenname = random.choice(utilites.halfling_given_name)
    #Assignes a title or surename based on the allignment
    if alligment_ply == "evil":
        fullname = givenname + random.choice(utilites.evil_titles)
    elif alligment_ply == "neutral":
        fullname =givenname + " " + surename
    elif alligment_ply == "good":
        fullname = givenname + random.choice(utilites.good_titles)
    return fullname

if name_ply == "random":
    name_ply = name_genrator()

def ideal_generator():
    #Generates randomised backgorund
    ideal_list = []
    ideal_list.append(utilites.IDEALS.get("all1"))
    ideal_list.append(utilites.IDEALS.get("all2"))
    #Selects one allignment convinient ideal
    if "chaotic" in selected_allignment:
        ideal_list.append(utilites.IDEALS.get("chaotic"))
        ideal_ply = random.choice(ideal_list)
    if "neutral" in selected_allignment:
        ideal_list.append(utilites.IDEALS.get("neutral"))
        ideal_ply = random.choice(ideal_list)
    if "good" in selected_allignment:
        ideal_list.append(utilites.IDEALS.get("good"))
        ideal_ply = random.choice(ideal_list)
    else:
        ideal_ply = random.choice(list(utilites.IDEALS.values()))
    return ideal_ply

background_ply =ideal_generator()

def create_summary():
    if porpuse == "npc" or porpuse == "player":
        if alligment_ply == "evil":
            summary_ply = f"{name_ply}" + f" was a feared {spices_ply}"
        elif alligment_ply == "neutral":
            summary_ply = f"{name_ply}" + f" was an fair {spices_ply}"
        elif alligment_ply == "good":
            summary_ply = f"{name_ply}" + f" was a wonderful {spices_ply}"
        if background_ply == "Knowledge":
            summary_ply = summary_ply + " who always seek Knowledge"
        elif background_ply == "Freedom":
            summary_ply = summary_ply + " who always fights for freedom"
        elif background_ply == "Hope":
            summary_ply = summary_ply + " who never loose hope"
        elif background_ply == "Self-Reliance":
            summary_ply = summary_ply + " who belives in self-reliance"
        elif background_ply == "Adaptability":
            summary_ply = summary_ply + " who is a true survivor"
    if porpuse == "villian":
        summary_ply = f"{name_ply}" + f" was a feared {spices_ply}"
        if background_ply == "Knowledge":
            summary_ply = summary_ply + " who always seek forbidden knowledge"
        elif background_ply == "Freedom":
            summary_ply = summary_ply + " who wanted his own freedom"
        elif background_ply == "Self-Reliance":
            summary_ply = summary_ply + " who never trusted anyone"
        elif background_ply == "Adaptability":
            summary_ply = summary_ply + " who survived so many tragedies"
    return summary_ply


summary_ply = create_summary()

def modifier_count():
        for i in skill_set_ply:
            if modifyer_set[i] >= 14:
                modifyer_set[i] = 2
            if 13 >= modifyer_set[i] >= 12:
                modifyer_set[i] = 1
            if 11 >= modifyer_set[i] >= 10:
                modifyer_set[i] = 0
            if 9 >= modifyer_set[i] >= 8:
                modifyer_set[i] = -1
        return modifyer_set


flaw_ply = random.choice(utilites.FLAWS)
bonds_ply = random.choice(utilites.BONDS)
person_ply = '\n'.join(random.sample(utilites.PERSONALITY_TRAIS, 2))
modifier_ply = modifier_count()
ideal_ply = background_ply

def character_dictonary(**kwargs):
    full_ply = skill_set_ply.copy()
    full_ply["name"] = name_ply
    full_ply["class"] = class_ply
    full_ply["flwas"] = name_ply
    full_ply["bonds"] = bonds_ply
    full_ply["ideal"] = ideal_ply
    return full_ply

npc_gen = character_dictonary()

f = open(f"{name_ply}.txt", "w")
f.write(("%s \n \n %s \n \n %s \n \n %s \n \n %s \n \n %s \n %s \n %s\n \n %s \n %s \n" % (name_ply, selected_allignment ,create_summary(), utilites.background_gener, "Ideals: " + ideal_ply, "Flaws: "+ flaw_ply,"Bonds: " + bonds_ply,"Prersonality traits: " + person_ply,skill_set_ply, modifier_ply)))
f.close()