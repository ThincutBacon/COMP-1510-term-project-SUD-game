"""

Kanon Nishiyama
A1415217

"""


def character():
    """
    Ask player to create a new character.

    :postcondition: promt the player to pick a name, species, and class for the character
    :postcondition: create a dictionary containing the character information and attributes
    :return: the dictionary

    >>> character()
    {}
    """
    new_character = {"name": "",
                     "species": "",
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
                     "x-coordinate": 0,
                     "y-coordinate": 0,
                     "kingdom": "",
                     "BBEG": ""}

    species_list = {"human": {"desc": "Although average in most aspects, they possess strong survival "
                                      "prowess and the ability to utilize items to their fullest potential.\n"
                                      "\n"
                                      "Highest Attributes: ATK and LUK\n"
                                      "Species Bonus: All items gain an additional +2 to their effects\n"
                                      "\n",
                              "HP": 0,
                              "SP": 0,
                              "ATK": 0,
                              "DEF": 0,
                              "AGI": 0,
                              "LUK": 0},
                    "elf": {"desc": "With their long life spans and equally cumulative knowledge, they are known "
                                    "to be the best when it comes to efficiently using skills and spells.\n"
                                    "\n"
                                    "Highest Attributes: SP and AGI\n"
                                    "Species Bonus: All skills cost -1 SP\n"
                                    "\n",
                            "HP": 0,
                            "SP": 0,
                            "ATK": 0,
                            "DEF": 0,
                            "AGI": 0,
                            "LUK": 0},
                    "dwarf": {"desc": "To withstand the frigid cold of the mountain tops and the sweltering "
                                      "heat of a forge, they have developed a thicker skin then many.\n"
                                      "\n"
                                      "Highest Attributes: HP and DEF\n"
                                      "Species Bonus: All equipment gain an additional +1 to their effects\n"
                                      "\n",
                              "HP": 0,
                              "SP": 0,
                              "ATK": 0,
                              "DEF": 0,
                              "AGI": 0,
                              "LUK": 0}}

    class_list = {"warrior": {"desc": "Warrior's ",
                              "skill_list": ["shield", "shield bash"]},
                  "scout": {"desc": "",
                            "skill_list": []},
                  "mage": {"desc": "",
                           "skill_list": []}}


    while True:
        new_character["kingdom"] = input("What is the name of your kingdom?: ")

        print("As heir to the throne of " + new_character["kingdom"] + ",")
        new_character["name"] = input("What is your name?: ")

        confirm_species = False
        while not confirm_species:
            print("HUMAN\n"
                  "\"The most versatile of species.\"\n"
                  "\n"
                  "ELF\n"
                  "\"The graceful guardians of the forests.\"\n"
                  "\n"
                  "DWARF\n"
                  "\"Inhabitants of the deepest caves and the highest mountains.\"\n"
                  "\n"
                  "\n")

            selected_species = input("Enter the species name for more information: ").lower()

            if selected_species in species_list.keys():
                print("\n\n" + selected_species.upper() + "\n" + species_list[selected_species]["desc"])
                while True:
                    confirm = input("Do you want to be a " + selected_species.upper() + "? (y/n): ").lower()
                    if confirm == "y":
                        new_character["species"] = selected_species
                        confirm_species = True
                        break
                    elif confirm == "n":
                        break
                    else:
                        print("Please confirm your selection.")
            else:
                print("Please enter a valid species!")

        confirm_class = False
        while not confirm_class:
            print("WARRIOR\n"
                  "\"\"\n"
                  "\n"
                  "SCOUT\n"
                  "\"\"\n"
                  "\n"
                  "MAGE\n"
                  "\"\"\n"
                  "\n"
                  "\n")

            selected_class = input("Enter the class name for more information: ").lower()

            if selected_class in class_list.keys():
                print("\n\n" + selected_class.upper() + "\n" + class_list[selected_class]["desc"])
                while True:
                    confirm = input("Do you want to be a " + selected_class.upper() + "? (y/n): ").lower()
                    if confirm == "y":
                        new_character["skill_class"] = selected_class
                        confirm_class = True
                        break
                    elif confirm == "n":
                        break
                    else:
                        print("Please confirm your selection.")
            else:
                print("Please enter a valid class!")

        confirm = input("Is this you? (y/n): ").lower()

        if confirm == "y":
            return new_character
        elif confirm == "n":
            continue
        else:
            print("Please confirm your character information.")


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
