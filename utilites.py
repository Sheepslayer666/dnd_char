import random

STANDARD_ARRAY = [15, 14, 13, 12, 10, 8]
CLASSES = ["barbarian", 'bard', "fighter" , "cleric", "druid", "monk", "paladin", "ranger", "rouge", "sourcerer", "warlock", "wizard"]
name_ply = ""
ALLIGNMENT_GOOD = ["Lawful good", "Neutral good", "Chaotic good"]
ALLIGNMENT_EVIL = ["Lawful evil", "Neutral evil", "Neutral evil"]
ALLIGNMENT_NEUT = ["Lawful neutral", "True Neutral", "Chaotic neutral"]
SKILLS = ["strenght", "dexterity", "intelligence", "wisdom", "charisma"]
SPECIES = ["Dwarf", "Elf", "Halfling", "Human"]
PERSONALITY_TRAIS = ["I always have a story from a faraway place.", "I observe more than I speak, but when I do, people listen.", "I see potential friends in everyone I meet.", 
"I keep a mental map of every place I visit.", "I live for the moment—planning is for others.", "I carry a token from someone I left behind and think of them often.",
"I’m suspicious of those who stay in one place too long.", "I journal everything—someone will want to read it one day." ]
IDEALS = {
    "chaotic" : "Freedom",
    "neutral" : "Knowledge",
    "good" : "Hope",
    "all1" : "Self-Reliance", 
    "all2" : "Adaptability"
}
FLAWS = ["I find it hard to stay in one place or with one group for too long.", "I embellish my stories… a lot.", 
"I trust too easily—or not at all.", "I avoid conflict, even when I should stand my ground.", "I’m haunted by memories of a past I try to forget."]
BONDS = ["I owe a great debt to someone who once saved my life.", "I’m searching for a place that truly feels like home."
, "I made a promise to someone and intend to keep it, no matter how far I roam.", "My journal contains the only record of a lost civilization.", "I once failed someone who depended on me, and I won’t let that happen again."]
human_given_name = ["Frederic", "Goldwyn", "Bob", "Billard", "Rudolf", "Bloodwyn", "Gomez"]
dwarf_given_name = ["Olin", "Brewin", "Dalin", "Thorin", "Thorlof", "Arnulf", ]
elf_given_name = ["Dalion", "Tylion", "Quillion", "Cyndrion"]
surenames_1 = ["Iron", "Horse", "Tree", "Beer", "Wolf", "Bow", "Light", "Fire", "Oak", "Deer", "Gold"]
surenames_2 = ["master", "caster", "killer", "foe", "hand", "frined", "traveller", "walker", "eater", "dreamer"]
evil_titles = [" the destroyer", " the wordeater", " the dreadful", " the imp"]
good_titles = [" the goodwilling", " the heavenly", " the great", " hero of the west"]
origin = ["a village", "a city", "a tavern", "a barn", "the wildernsess"]
places = ["tavern", "smallhold", "mansion", "house"]
problems = ["beaten by ", "into the debt of ", "a bad fight with "]
cause = ["the vampires", "the mayor", "a small group of goblins", "a lonely necromancer", "a group of bantis"]
background_gener = f"""He was born in {random.choice(origin)}, had to leave his family's beloved {random.choice(places)}, becuse of the 
unexpected event of getting {random.choice(problems)}{random.choice(cause)}"""
