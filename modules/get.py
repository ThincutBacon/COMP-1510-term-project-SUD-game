"""

Kanon Nishiyama
A1415217

"""


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
                             "You see a glint of something in the corner of your eye.\n"
                             "Maybe you could SCAVENGE to see what it is.",
                     "area": "safe",
                     "scavenge": "key",
                     "action": "none",
                     "walls": ["n", "s", "w"]},
            (0, 1): {"name": "The Dungeons - The Exit",
                     "look": "Your only exit lies in front of you, locked and guarded from outside.\n"
                             "Once you EXIT, you are sure to enter battle with the guards.",
                     "area": "safe",
                     "scavenge": "none",
                     "action": "exit",
                     "walls": ["n", "s", "e"]}}


def main_board():
    """
    Return the main board.

    :return: a dictionary containing tuples containing coordinates as keys which are paired with a dictionary
             containing the coordinates information

    >>> main_board() #doctest: +ELLIPSIS
    {(0, 0): {'name': 'The Dungeons - Hallway', 'look': 'What is left of the dungeons is a shell ...
    """
    return {(0, 0): {"name": "The Dungeons - Hallway",
                     "look": "What is left of the dungeons is a shell of what used to confine you. "
                             "Only rats roam these halls now.",
                     "area": "dungeon",
                     "scavenge": "none",
                     "action": "none",
                     "walls": ["n", "s", "w"]},
            (0, 1): {"name": "The Dungeons - The Exit",
                     "look": "The slain bodies of the guards remain discarded next to the door.",
                     "area": "safe",
                     "scavenge": "none",
                     "action": "none",
                     "walls": ["n", "e"]},
            (0, 2): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (0, 3): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (0, 4): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},

            (1, 0): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (1, 1): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (1, 2): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (1, 3): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (1, 4): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},

            (2, 0): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (2, 1): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (2, 2): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (2, 3): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (2, 4): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},

            (3, 0): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (3, 1): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (3, 2): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (3, 3): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (3, 4): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},

            (4, 0): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (4, 1): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (4, 2): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (4, 3): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (4, 4): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []}}


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
