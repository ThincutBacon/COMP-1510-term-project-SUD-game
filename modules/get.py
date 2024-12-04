"""

Kanon Nishiyama
A1415217

"""

import random

from colorama import Style, Fore

from select import select


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
            "modifiers": {"HP": 0, "SP": 0, "ATK": 0, "DEF": 0, "AGI": 0, "LUK": 0},
            "equipment": {"head": "", "chest": "", "legs": "", "feet": "", "weapon": ""},
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
    Return species information.

    :param select: a string
    :precondition: select must equal None or one of the keys within entire_species_list
    :return: if select equals None, returns the entire dictionary
    :return: if select equals a key, returns a single species dictionary

    >>> species_list() #doctest: +ELLIPSIS
    {'list_all': '==========...
    >>> species_list("elf") #doctest: +ELLIPSIS
    {'name': 'elf', 'desc': 'With their long life spans and equally cumulative knowledge...
    """
    entire_species_list = {"list_all": "==========\n" +
                                       Style.BRIGHT + "HUMAN\n" + Style.RESET_ALL +
                                       "\"The most versatile of species.\"\n"
                                       "\n" +
                                       Style.BRIGHT + "ELF\n" + Style.RESET_ALL +
                                       "\"The graceful guardians of the forests.\"\n"
                                       "\n" +
                                       Style.BRIGHT + "DWARF\n" + Style.RESET_ALL +
                                       "\"Inhabitants of the deepest caves and the highest mountains.\"\n"
                                       "==========\n",
                           "human": {"name": "human",
                                     "adjective": "human",
                                     "desc": "Although average in most aspects, they possess strong survival \n"
                                             "prowess and the ability to utilize items to their fullest potential.\n"
                                             "\n"
                                             f"{Style.BRIGHT}Highest Attributes:{Style.RESET_ALL} ATK and LUK\n"
                                             f"{Style.BRIGHT}Species Bonus:{Style.RESET_ALL} All items gain an "
                                             f"additional +2 to their effects\n",
                                     "HP": 0,
                                     "SP": 0,
                                     "ATK": 0,
                                     "DEF": 0,
                                     "AGI": 0,
                                     "LUK": 0},
                           "elf": {"name": "elf",
                                   "adjective": "elven",
                                   "desc": "With their long life spans and equally cumulative knowledge, they are \n"
                                           "known to be the best when it comes to efficiently using skills and \n"
                                           "spells.\n"
                                           "\n"
                                           f"{Style.BRIGHT}Highest Attributes:{Style.RESET_ALL} SP and AGI\n"
                                           f"{Style.BRIGHT}Species Bonus:{Style.RESET_ALL} All skills cost -1 SP\n",
                                   "HP": 0,
                                   "SP": 0,
                                   "ATK": 0,
                                   "DEF": 0,
                                   "AGI": 0,
                                   "LUK": 0},
                           "dwarf": {"name": "dwarf",
                                     "adjective": "dwarven",
                                     "desc": "To withstand the frigid cold of the mountain tops and the sweltering \n"
                                             "heat of a forge, they have developed a thicker skin then many.\n"
                                             "\n"
                                             f"{Style.BRIGHT}Highest Attributes:{Style.RESET_ALL} HP and DEF\n"
                                             f"{Style.BRIGHT}Species Bonus:{Style.RESET_ALL} All equipment gain "
                                             f"an additional +1 to their effects\n",
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
    Return class information.

    :param select: a string
    :precondition: select must equal None or one of the keys within entire_class_list
    :return: if select equals None, returns the entire dictionary
    :return: if select equals a key, returns a single class dictionary

    >>> class_list() #doctest: +ELLIPSIS
    {'list_all': '==========...
    >>> class_list("mage") #doctest: +ELLIPSIS
    {'class': 'mage', 'desc': "Mage's fight a careful battle, slowly chipping away at their ...
    """
    entire_class_list = {"list_all": "==========\n" +
                                     Style.BRIGHT + "WARRIOR\n" + Style.RESET_ALL +
                                     "\"For those who fight with endurance.\"\n"
                                     "\n" +
                                     Style.BRIGHT + "SCOUT\n" + Style.RESET_ALL +
                                     "\"For those who fight with deadly accuracy.\"\n"
                                     "\n" +
                                     Style.BRIGHT + "MAGE\n" + Style.RESET_ALL +
                                     "\"For those who fight by leveling the playing field.\"\n"
                                     "==========\n",
                         "warrior": {"class": "warrior",
                                     "desc": "Warrior's fight slow battles with a shield in hand, toughing it \n"
                                             "out until their enemies fall in battle.\n"
                                             "\n"
                                             f"{Style.BRIGHT}Class Skills:{Style.RESET_ALL}\n"
                                             f"{Style.BRIGHT}Shield{Style.RESET_ALL} - Increases your DEF\n"
                                             f"{Style.BRIGHT}Shield Bash{Style.RESET_ALL} - Attacks while raising "
                                             f"your DEF\n"
                                             f"{Style.BRIGHT}Battle Cry{Style.RESET_ALL} - Weakens enemy DEF\n",
                                     "skill_list": ["shield", "shield bash", "battle cry"]},
                         "scout": {"class": "scout",
                                   "desc": "Scout's fight quick battles, inflicting fatal damage before their \n"
                                           "enemies have a chance to hurt them back.\n"
                                           "\n"
                                           f"{Style.BRIGHT}Class Skills:{Style.RESET_ALL}\n"
                                           f"{Style.BRIGHT}Sharper Edge{Style.RESET_ALL} - Increases your ATK\n"
                                           f"{Style.BRIGHT}Focus Attack{Style.RESET_ALL} - Attacks while increasing "
                                           f"your LUK\n"
                                           f"{Style.BRIGHT}Haste{Style.RESET_ALL} - Increases your AGI\n",
                                   "skill_list": ["sharper edge", "focus attack", "haste"]},
                         "mage": {"class": "mage",
                                  "desc": "Mage's fight a careful battle, slowly chipping away at their enemies \n"
                                          "health while maintaining their own.\n"
                                          "\n"
                                          f"{Style.BRIGHT}Class Skills:{Style.RESET_ALL}\n"
                                          f"{Style.BRIGHT}Fireball{Style.RESET_ALL} - Continuously burns the enemy\n"
                                          f"{Style.BRIGHT}Freezing Touch{Style.RESET_ALL} - Slows an enemy's AGI\n"
                                          f"{Style.BRIGHT}Healing Light{Style.RESET_ALL} - Heals your HP\n",
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
                     "look": "There is no light inside the dark cavernous halls of the dungeons, \n"
                             "the only sliver of light pours in from the slits of the door which \n"
                             "withholds your freedom.\n"
                             "\n"
                             "You can hear footsteps heading your way.\n"
                             f"If you continue {Fore.GREEN}{Style.BRIGHT}EAST{Style.RESET_ALL}, you are sure to "
                             f"enter battle with the \n"
                             "guards.\n",
                     "area": "safe",
                     "walls": ["n", "s", "w"]},
            (0, 1): {"name": "The Dungeons - The Exit",
                     "look": "You shouldn't be able to access this.",
                     "area": "tutorial",
                     "symbol": "exit",
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
                         "look": "What is left of the dungeons is a shell of what used to confine \n"
                                 "you. \n"
                                 "Only rats roam these halls now.\n",
                         "area": "dungeon",
                         "walls": ["n", "s", "w"]},
                (0, 1): {"name": "The Dungeons - The Exit",
                         "look": "The slain bodies of the guards remain discarded next to the door.\n",
                         "area": "dungeon",
                         "walls": ["n", "e"]},
                (0, 2): {"name": "The Forest - The Castle Walls",
                         "look": "You can observe the wide expanse of the castle walls from here. \n"
                                 "The walls usually guarded by the castle guards now only house an \n"
                                 "eerie silence.\n",
                         "area": "field",
                         "walls": ["n", "w"]},
                (0, 3): {"name": "The Forest - The Castle Walls",
                         "look": "You can observe the wide expanse of the castle walls from here. \n"
                                 "The walls usually guarded by the castle guards now only house an \n"
                                 "eerie silence.\n",
                         "area": "field",
                         "walls": ["n"]},
                (0, 4): {"name": "The Forest - The Castle Gates",
                         "look": "In front of you are the back gates that lead into the castle grounds. \n"
                                 "Moss covers it's entirety from lack of use. From here you can sneak \n"
                                 "into the castle grounds to confront the false king.\n",
                         "area": "field",
                         "symbol": "exit",
                         "walls": ["n", "e"]},

                (1, 0): {"name": "The Forest - Outer Edge",
                         "look": "",
                         "area": "field",
                         "walls": ["w"]},
                (1, 1): {"name": "The Forest - Outside The Dungeon",
                         "look": "Right outside of the dungeons expands a wide, limitless forest. Here \n"
                                 "lives a diverse range of creatures, both predator and prey. You can \n"
                                 "spot the \n"
                                 f"start of a faint path to the {Fore.GREEN}{Style.BRIGHT}EAST{Style.RESET_ALL}.\n",
                         "area": "field",
                         "walls": []},
                (1, 2): {"name": "The Forest - A Faint Path",
                         "look": f"The faint path seems to continue onto the {Fore.GREEN}{Style.BRIGHT}EAST"
                                 f"{Style.RESET_ALL}.\n",
                         "area": "field",
                         "walls": []},
                (1, 3): {"name": "The Forest - A Faint Path",
                         "look": f"The faint path seems to extend to the {Fore.GREEN}{Style.BRIGHT}WEST"
                                 f"{Style.RESET_ALL} "
                                 f"and {Fore.GREEN}{Style.BRIGHT}EAST{Style.RESET_ALL}. To the "
                                 f"{Fore.GREEN}{Style.BRIGHT}SOUTH{Style.RESET_ALL} seems to \n"
                                 "stretch a clearer path.\n",
                         "area": "field",
                         "walls": []},
                (1, 4): {"name": "The Forest - A Faint Path",
                         "look": f"The faint path seems to extend to the {Fore.GREEN}{Style.BRIGHT}WEST"
                                 f"{Style.RESET_ALL} "
                                 f"and {Fore.GREEN}{Style.BRIGHT}NORTH{Style.RESET_ALL}.\n",
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
                         "look": f"The path seems to extend to the {Fore.GREEN}{Style.BRIGHT}NORTH"
                                 f"{Style.RESET_ALL} and "
                                 f"{Fore.GREEN}{Style.BRIGHT}SOUTH{Style.RESET_ALL}.\n",
                         "area": "field",
                         "walls": []},
                (2, 4): {"name": "The Forest - Outer Edge",
                         "look": "",
                         "area": "field",
                         "walls": ["e"]},

                (3, 0): {"name": "Deep Forest - Home To Danger",
                         "look": "Here, deep in the forest, lives creatures much more stronger, \n"
                                 "fiercer, and dangerous then those near the outer rim.\n",
                         "area": "forest",
                         "symbol": "danger",
                         "walls": ["w"]},
                (3, 1): {"name": "Deep Forest - Home To Danger",
                         "look": "Here, deep in the forest, lives creatures much more stronger, \n"
                                 "fiercer, and dangerous then those near the outer rim.\n",
                         "area": "forest",
                         "symbol": "danger",
                         "walls": []},
                (3, 2): {"name": "The Forest - Deep Within",
                         "look": "",
                         "area": "field",
                         "walls": []},
                (3, 3): {"name": "The Forest - Village Path",
                         "look": f"The path seems to extend to the {Fore.GREEN}{Style.BRIGHT}NORTH"
                                 f"{Style.RESET_ALL} "
                                 f"and {Fore.GREEN}{Style.BRIGHT}SOUTH{Style.RESET_ALL}.\n"
                                 "You can observe a small village to the SOUTH.\n",
                         "area": "field",
                         "walls": []},
                (3, 4): {"name": "The Village - Outer End",
                         "look": "From the outer end of the village, you can observe an expanse \n"
                                 "of trees that create the forest beyond.\n"
                                 f"To the {Fore.GREEN}{Style.BRIGHT}SOUTH{Style.RESET_ALL} you can "
                                 f"hear the hustle and "
                                 "bustle of the village square.\n",
                         "area": "safe",
                         "symbol": "shop",
                         "shop": "weapon",
                         "walls": ["e"]},

                (4, 0): {"name": "Deep Forest - Home To Danger",
                         "look": "Here, deep in the forest, lives creatures much more stronger, \n"
                                 "fiercer, and dangerous then those near the outer rim.\n",
                         "area": "forest",
                         "symbol": "danger",
                         "walls": ["w", "s"]},
                (4, 1): {"name": "Deep Forest - Home To Danger",
                         "look": "Here, deep in the forest, lives creatures much more stronger, \n"
                                 "fiercer, and dangerous then those near the outer rim.\n",
                         "area": "forest",
                         "symbol": "danger",
                         "walls": ["s"]},
                (4, 2): {"name": "The Forest - Deep Within",
                         "look": "",
                         "area": "field",
                         "walls": ["s"]},
                (4, 3): {"name": "The Village - Outer End",
                         "look": "From the outer end of the village, you can observe an expanse \n"
                                 "of trees that create the forest beyond.\n"
                                 f"To the {Fore.GREEN}{Style.BRIGHT}EAST{Style.RESET_ALL} you can hear the hustle and "
                                 f"bustle of the village square.\n",
                         "area": "safe",
                         "symbol": "shop",
                         "shop": "item",
                         "walls": ["s"]},
                (4, 4): {"name": "The Village - The Market",
                         "look": "You can see the a variety of shop owners keeping shop, shouting out to \n"
                                 "patrons to appeal their products.\n"
                                 "You could SHOP here to buy equipment or sell the items you carry.\n",
                         "area": "safe",
                         "symbol": "shop",
                         "shop": "equipment",
                         "walls": ["e", "s"]}}

    field_descriptions = [
        "A gentle breeze rustle through the surrounding foliage.\n",
        "You can spot the tail end of a deer as it quickly springs away from \n"
        "you.\n",
        "You can spot the occasional berry bush housing unnervingly red berries.\n",
        "You spot a group of mushrooms growing in the shade. No matter how \n"
        "hungry you are, you better avoid them if you intend to survive.\n",
        "The path you follow is non-existent, only a suggestion carved by nature \n"
        "itself.\n"
    ]

    for square in main_map.keys():
        if main_map[square]["look"] == "" and main_map[square]["area"] == "field":
            main_map[square]["look"] = random.choice(field_descriptions)

    return main_map


def command_list(group_select=None, command_select=None):
    """
    Return player command information.

    :param group_select: a string
    :param command_select: a string
    :precondition: group_select must equal None or one of the keys within all_commands_list
    :precondition: command_select must equal None or one of the keys within either "explore" or "battle"
    :return: if group_select and command_select equals None, return the entire dictionary
    :return: if group_select equals a key and command_select equals None, return "explore" or "battle" dictionary
    :return: if group_select and command_select equals a key, returns a single command dictionary

    >>> command_list() #doctest: +ELLIPSIS
    {'list_all': '==========...
    >>> command_list("elf") #doctest: +ELLIPSIS
    {'name': 'elf', 'desc': 'With their long life spans and equally cumulative knowledge...
    """
    all_commands_list = {"explore": {},
                         "battle": {}}

    if command_select:
        return all_commands_list[group_select][command_select]
    elif group_select:
        return all_commands_list[select]
    else:
        return all_commands_list


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
