"""

Kanon Nishiyama
A1415217

"""
from modules import get


def character():
    """
    Ask player to create a new character.

    :postcondition: promt the player to pick a names, species, and class for the character
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
                     "equipment": {"head": "", "chest": "", "legs": "", "feet": ""},
                     "x-coordinate": 0,
                     "y-coordinate": 0,
                     "kingdom": "",
                     "BBEG": ""}

    class_list = {"list_all": "==========\n"
                              "WARRIOR\n"
                              "\"For those who fight with endurance.\"\n"
                              "\n"
                              "SCOUT\n"
                              "\"For those who fight with deadly accuracy.\"\n"
                              "\n"
                              "MAGE\n"
                              "\"For those who fight by leveling the playing field.\"\n"
                              "==========\n",
                  "warrior": {"desc": "Warrior's fight slow battles with a shield in hand, toughing it "
                                      "out until their enemies fall in battle.\n"
                                      "\n"
                                      "Class Skills:\n"
                                      "Shield - Increases your DEF\n"
                                      "Shield Bash - Attacks while raising your DEF\n"
                                      "Battle Cry - Weakens enemy DEF\n",
                              "skill_list": ["shield", "shield bash", "battle cry"]},
                  "scout": {"desc": "Scout's fight quick battles, inflicting fatal damage before their "
                                    "enemies have a chance to hurt them back.\n"
                                    "\n"
                                    "Class Skills:\n"
                                    "Sharper Edge - Increases your ATK\n"
                                    "Focus Attack - Attacks while increasing your LUK\n"
                                    "Haste - Increases your AGI\n",
                            "skill_list": ["sharper edge", "focus attack", "haste"]},
                  "mage": {"desc": "Mage's fight a careful battle, slowly chipping away at their enemies "
                                   "health while maintaining their own.\n"
                                   "\n"
                                   "Class Skills:\n"
                                   "Fireball - Continuously burns the enemy\n"
                                   "Freezing Touch - Slows an enemy's AGI\n"
                                   "Healing Light - Heals your HP\n",
                           "skill_list": ["fireball", "freezing touch", "healing light"]}}

    confirm_kingdom = False
    while not confirm_kingdom:
        kingdom_name = input("\n\n\nWhat is the name of your kingdom?: ")
        if kingdom_name != "":
            new_character["kingdom"] = kingdom_name
            confirm_kingdom = True
        else:
            print("\n\n\nPlease enter a name for your kingdom!")

    confirm_character_name = False
    while not confirm_character_name:
        print("\n\n\nAs heir to the throne of " + new_character["kingdom"].upper() + ",")
        character_name = input("What is your name?: ")
        if character_name != "":
            new_character["name"] = character_name
            confirm_character_name = True
        else:
            print("\n\n\nPlease enter a name for your kingdom!")

    confirm_species = False
    while not confirm_species:
        print("\n\n\n" + get.species_list("list_all"))

        selected_species = input("Enter the species name for more information: ").lower()
        if selected_species in get.species_list().keys():
            print("\n\n\n"
                  "==========\n" +
                  get.species_list(selected_species)["name"].upper() + "\n"
                  "\n" +
                  get.species_list(selected_species)["desc"] +
                  "==========\n")
            while True:
                confirm = input("Do you want to be a " + selected_species.upper() + "? (y/n): ").lower()
                if confirm == "y":
                    new_character["species"] = selected_species
                    confirm_species = True
                    break
                elif confirm == "n":
                    break
                else:
                    print("\n\n\nPlease confirm your selection.\n\n\n")
        else:
            print("\n\n\nPlease enter a valid species!")

    confirm_class = False
    while not confirm_class:
        print("\n\n\n" + class_list["list_all"])

        selected_class = input("Enter the class name for more information: ").lower()
        if selected_class in class_list.keys():
            print("\n\n\n"
                  "==========\n" +
                  selected_class.upper() + "\n"
                  "\n" +
                  class_list[selected_class]["desc"] +
                  "==========\n")
            while True:
                confirm = input("Do you want to be a " + selected_class.upper() + "? (y/n): ").lower()
                if confirm == "y":
                    new_character["skill_class"] = selected_class
                    confirm_class = True
                    break
                elif confirm == "n":
                    break
                else:
                    print("\n\n\nPlease confirm your selection.\n\n\n")
        else:
            print("\n\n\nPlease enter a valid class!")

    confirm_new_character = False
    while not confirm_new_character:
        print("\n\n\n"
              "==========\n"
              "Kingdom: " + new_character["kingdom"] + "\n"
              "Name: " + new_character["name"] + "\n"
              "\n"
              "Species: " + new_character["species"].title() + "\n"
              "Class: " + new_character["skill_class"].title() + "\n"
              "==========\n")
        confirm = input("Is this the character you want to create? (y/n): ").lower()
        if confirm == "y":
            return new_character
        elif confirm == "n":
            character()
        else:
            print("\n\n\nPlease confirm your character information.")


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
    character()


if __name__ == "__main__":
    main()
