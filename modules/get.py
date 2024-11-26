"""

Kanon Nishiyama
A1415217

"""
import random


def blank_character():
    """
    Returns a blank character.

    :return: a dictionary containing default charater information

    >>> blank_character() #doctest: +ELLIPSIS
    {'name': '', 'species': '', 'skill_class': '', 'LVL': 1, 'EXP': 0, ...
    """
    return {"kingdom": "",
            "name": "",
            "species": "",
            "species_adjective": "",
            "skill_class": "",
            "LVL": 1,
            "EXP": 0,
            "max_HP": 0,
            "current_HP": 0,
            "max_SP": 0,
            "current_SP": 0,
            "ATK": 0,
            "DEF": 0,
            "AGI": 0,
            "LUK": 0,
            "equipment": {"head": "", "chest": "", "legs": "", "feet": ""},
            "inventory": {},
            "x-coordinate": 0,
            "y-coordinate": 0,
            "coins": 0}


def unnamed_bbeg():
    """
    Returns the unnamed BBEG.

    :return: a dictionary containing default BBEG information

    >>> unnamed_bbeg() #doctest: +ELLIPSIS
    {'name': '', 'max_HP': 0, 'current_HP': 0, 'max_SP': 0,...
    """
    return {"name": "",
            "max_HP": 0,
            "current_HP": 0,
            "max_SP": 0,
            "current_SP": 0,
            "ATK": 0,
            "DEF": 0,
            "AGI": 0,
            "LUK": 0}


def species_list(select=None):
    """
    Returns species information.

    :param select: a string
    :precondition: select must equal None or one of the keys within entire_species_list
    :return: if select equals None, returns the entire dictionary
    :return: if select equals a key, returns a single species dictionary

    >>> species_list() #doctest: +ELLIPSIS
    {'list_all': '==========...
    >>> species_list("elf") #doctest: +ELLIPSIS
    {'name': 'elf', 'desc': 'With their long life spans and equally cumulative knowledge...
    """
    entire_species_list = {"list_all": "==========\n"
                                       "HUMAN\n"
                                       "\"The most versatile of species.\"\n"
                                       "\n"
                                       "ELF\n"
                                       "\"The graceful guardians of the forests.\"\n"
                                       "\n"
                                       "DWARF\n"
                                       "\"Inhabitants of the deepest caves and the highest mountains.\"\n"
                                       "==========\n",
                           "human": {"name": "human",
                                     "adjective": "human",
                                     "desc": "Although average in most aspects, they possess strong survival "
                                             "prowess and the ability to utilize items to their fullest potential.\n"
                                             "\n"
                                             "Highest Attributes: ATK and LUK\n"
                                             "Species Bonus: All items gain an additional +2 to their effects\n",
                                     "HP": 0,
                                     "SP": 0,
                                     "ATK": 0,
                                     "DEF": 0,
                                     "AGI": 0,
                                     "LUK": 0},
                           "elf": {"name": "elf",
                                   "adjective": "elven",
                                   "desc": "With their long life spans and equally cumulative knowledge, they are "
                                           "known to be the best when it comes to efficiently using skills and "
                                           "spells.\n"
                                           "\n"
                                           "Highest Attributes: SP and AGI\n"
                                           "Species Bonus: All skills cost -1 SP\n",
                                   "HP": 0,
                                   "SP": 0,
                                   "ATK": 0,
                                   "DEF": 0,
                                   "AGI": 0,
                                   "LUK": 0},
                           "dwarf": {"name": "dwarf",
                                     "adjective": "dwarven",
                                     "desc": "To withstand the frigid cold of the mountain tops and the sweltering "
                                             "heat of a forge, they have developed a thicker skin then many.\n"
                                             "\n"
                                             "Highest Attributes: HP and DEF\n"
                                             "Species Bonus: All equipment gain an additional +1 to their effects\n",
                                     "HP": 0,
                                     "SP": 0,
                                     "ATK": 0,
                                     "DEF": 0,
                                     "AGI": 0,
                                     "LUK": 0}}

    if select:
        return entire_species_list[select]
    else:
        return entire_species_list


def class_list(select=None):
    """
    Returns class information.

    :param select: a string
    :precondition: select must equal None or one of the keys within entire_class_list
    :return: if select equals None, returns the entire dictionary
    :return: if select equals a key, returns a single class dictionary

    >>> class_list() #doctest: +ELLIPSIS
    {'list_all': '==========...
    >>> class_list("mage") #doctest: +ELLIPSIS
    {'class': 'mage', 'desc': "Mage's fight a careful battle, slowly chipping away at their ...
    """
    entire_class_list = {"list_all": "==========\n"
                                     "WARRIOR\n"
                                     "\"For those who fight with endurance.\"\n"
                                     "\n"
                                     "SCOUT\n"
                                     "\"For those who fight with deadly accuracy.\"\n"
                                     "\n"
                                     "MAGE\n"
                                     "\"For those who fight by leveling the playing field.\"\n"
                                     "==========\n",
                         "warrior": {"class": "warrior",
                                     "desc": "Warrior's fight slow battles with a shield in hand, toughing it "
                                             "out until their enemies fall in battle.\n"
                                             "\n"
                                             "Class Skills:\n"
                                             "Shield - Increases your DEF\n"
                                             "Shield Bash - Attacks while raising your DEF\n"
                                             "Battle Cry - Weakens enemy DEF\n",
                                     "skill_list": ["shield", "shield bash", "battle cry"]},
                         "scout": {"class": "scout",
                                   "desc": "Scout's fight quick battles, inflicting fatal damage before their "
                                           "enemies have a chance to hurt them back.\n"
                                           "\n"
                                           "Class Skills:\n"
                                           "Sharper Edge - Increases your ATK\n"
                                           "Focus Attack - Attacks while increasing your LUK\n"
                                           "Haste - Increases your AGI\n",
                                   "skill_list": ["sharper edge", "focus attack", "haste"]},
                         "mage": {"class": "mage",
                                  "desc": "Mage's fight a careful battle, slowly chipping away at their enemies "
                                          "health while maintaining their own.\n"
                                          "\n"
                                          "Class Skills:\n"
                                          "Fireball - Continuously burns the enemy\n"
                                          "Freezing Touch - Slows an enemy's AGI\n"
                                          "Healing Light - Heals your HP\n",
                                  "skill_list": ["fireball", "freezing touch", "healing light"]}}

    if select:
        return entire_class_list[select]
    else:
        return entire_class_list


def tutorial_board():
    """
    Return the tutorial board.

    :return: a dictionary containing tuples containing coordinates as keys which are paired with a dictionary
             containing the coordinates information

    >>> tutorial_board() #doctest: +ELLIPSIS
    {(0, 0): {'name': 'The Dungeons - Hallway', 'look': 'There is no light inside the dark ...
    """
    return {(0, 0): {"name": "The Dungeons - Hallway",
                     "look": "There is no light inside the dark cavernous halls of the dungeons, "
                             "the only sliver of light pours in from the slits of the door which withholds "
                             "your freedom.\n"
                             "You can hear footsteps heading your way.\n"
                             "If you continue forward, you are sure to enter battle with the guards.",
                     "area": "safe",
                     "walls": ["n", "s", "w"]},
            (0, 1): {"name": "The Dungeons - The Exit",
                     "look": "Your only exit lies in front of you, locked and guarded from outside.\n"
                             "Once you EXIT, you are sure to enter battle with the guards.",
                     "area": "tutorial",
                     "walls": ["n", "s", "e"]}}


def main_board():
    """
    Return the main board.

    :return: a dictionary containing tuples containing coordinates as keys which are paired with a dictionary
             containing the coordinates information

    >>> main_board() #doctest: +ELLIPSIS
    {(0, 0): {'name': 'The Dungeons - Hallway', 'look': 'What is left of the dungeons is a shell ...
    """
    main_map = {(0, 0): {"name": "The Dungeons - Hallway",
                         "look": "What is left of the dungeons is a shell of what used to confine you. "
                                 "Only rats roam these halls now.",
                         "area": "dungeon",
                         "walls": ["n", "s", "w"]},
                (0, 1): {"name": "The Dungeons - The Exit",
                         "look": "The slain bodies of the guards remain discarded next to the door.",
                         "area": "dungeon",
                         "walls": ["n", "e"]},
                (0, 2): {"name": "The Forest - The Castle Walls",
                         "look": "You can observe the wide expanse of the castle walls from here. "
                                 "The walls usually guarded by the castle guards now only house an "
                                 "eerie silence.",
                         "area": "field",
                         "walls": ["n", "w"]},
                (0, 3): {"name": "The Forest - The Castle Walls",
                         "look": "You can observe the wide expanse of the castle walls from here. "
                                 "The walls usually guarded by the castle guards now only house an "
                                 "eerie silence.",
                         "area": "field",
                         "walls": ["n"]},
                (0, 4): {"name": "The Forest - The Castle Gates",
                         "look": "In front of you are the back gates that lead into the castle grounds. "
                                 "Moss covers it's entirety from lack of use. From here you can sneak into "
                                 "the castle grounds to confront the false king.",
                         "area": "field",
                         "walls": ["n", "e"]},

                (1, 0): {"name": "The Forest - Outer Edge",
                         "look": "",
                         "area": "field",
                         "walls": ["w"]},
                (1, 1): {"name": "The Forest - Outside The Dungeon",
                         "look": "Right outside of the dungeons expands a wide, limitless forest. Here lives "
                                 "a diverse range of creatures, both predator and prey. You can spot the "
                                 "start of a faint path to the EAST.",
                         "area": "field",
                         "walls": []},
                (1, 2): {"name": "The Forest - A Faint Path",
                         "look": "The faint path seems to continue onto the EAST.",
                         "area": "field",
                         "walls": []},
                (1, 3): {"name": "The Forest - A Faint Path",
                         "look": "The faint path seems to extend to the WEST and EAST. To the SOUTH seems to "
                                 "stretch a clearer path",
                         "area": "field",
                         "walls": []},
                (1, 4): {"name": "The Forest - A Faint Path",
                         "look": "The faint path seems to extend to the WEST and NORTH.",
                         "area": "field",
                         "walls": ["e"]},

                (2, 0): {"name": "The Forest - Deep Within",
                         "look": "",
                         "area": "field",
                         "walls": ["w"]},
                (2, 1): {"name": "The Forest - Deep Within",
                         "look": "",
                         "area": "field",
                         "walls": []},
                (2, 2): {"name": "The Forest - Deep Within",
                         "look": "",
                         "area": "field",
                         "walls": []},
                (2, 3): {"name": "The Forest - Clear Path",
                         "look": "The path seems to extend to the NORTH and SOUTH.",
                         "area": "field",
                         "walls": []},
                (2, 4): {"name": "The Forest - Outer Edge",
                         "look": "",
                         "area": "field",
                         "walls": ["e"]},

                (3, 0): {"name": "Deep Forest - Home To Danger",
                         "look": "Here, deep in the forest, lives creatures much more stronger, "
                                 "fiercer, and dangerous then those near the outer rim.",
                         "area": "forest",
                         "walls": ["w"]},
                (3, 1): {"name": "Deep Forest - Home To Danger",
                         "look": "Here, deep in the forest, lives creatures much more stronger, "
                                 "fiercer, and dangerous then those near the outer rim.",
                         "area": "forest",
                         "walls": []},
                (3, 2): {"name": "The Forest - Deep Within",
                         "look": "",
                         "area": "field",
                         "walls": []},
                (3, 3): {"name": "The Forest - Village Path",
                         "look": "The path seems to extend to the NORTH and SOUTH.\n"
                                 "You can observe a small village to the SOUTH.",
                         "area": "field",
                         "walls": []},
                (3, 4): {"name": "The Village - Outer End",
                         "look": "From the outer end of the village, you can observe an expanse "
                                 "of trees that create the forest beyond.\n"
                                 "To the SOUTH you can hear the hustle and bustle of the village square.",
                         "area": "safe",
                         "walls": ["e"]},

                (4, 0): {"name": "Deep Forest - Home To Danger",
                         "look": "Here, deep in the forest, lives creatures much more stronger, "
                                 "fiercer, and dangerous then those near the outer rim.",
                         "area": "forest",
                         "walls": ["w", "s"]},
                (4, 1): {"name": "Deep Forest - Home To Danger",
                         "look": "Here, deep in the forest, lives creatures much more stronger, "
                                 "fiercer, and dangerous then those near the outer rim.",
                         "area": "forest",
                         "walls": ["s"]},
                (4, 2): {"name": "The Forest - Deep Within",
                         "look": "",
                         "area": "field",
                         "walls": ["s"]},
                (4, 3): {"name": "The Village - Outer End",
                         "look": "From the outer end of the village, you can observe an expanse "
                                 "of trees that create the forest beyond.\n"
                                 "To the EAST you can hear the hustle and bustle of the village square.",
                         "area": "safe",
                         "walls": ["s"]},
                (4, 4): {"name": "The Village - The Market",
                         "look": "You can see the a variety of shop owners keeping shop, shouting out to "
                                 "patrons to appeal their products.\n"
                                 "You could SHOP here to buy equipment or sell the items you carry.",
                         "area": "safe",
                         "walls": ["e", "s"]}}

    field_descriptions = [
        "A gentle breeze rustle through the surrounding foliage.",
        "You can spot the tail end of a deer as it quickly springs away from you.",
        "You can spot the occasional berry bush housing unnervingly red berries.",
        "You spot a group of mushrooms growing in the shade. No matter how hungry you are, "
        "you better avoid them if you intend to survive.",
        "The path you follow is non-existent, only a suggestion carved by nature itself."
    ]

    for square in main_map.keys():
        if main_map[square]["look"] == "" and main_map[square]["area"] == "field":
            main_map[square]["look"] = random.choice(field_descriptions)

    return main_map


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
