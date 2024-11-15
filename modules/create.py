"""

Kanon Nishiyama
A1415217

"""
from modules import get


def character():
    """
    Ask player to create a new character.

    :postcondition: prompt the player to pick a names, a species, and a class for the character
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

    confirm_kingdom = False
    while not confirm_kingdom:
        kingdom_name = input("\n\n\nWhat is the name of your kingdom?: ").strip()
        if kingdom_name != "":
            new_character["kingdom"] = kingdom_name
            confirm_kingdom = True
        else:
            print("\n\n\nPlease enter a name for your kingdom!")

    confirm_character_name = False
    while not confirm_character_name:
        print("\n\n\nAs heir to the throne of " + new_character["kingdom"].upper() + ",")
        character_name = input("What is your name?: ").strip()
        if character_name != "":
            new_character["name"] = character_name
            confirm_character_name = True
        else:
            print("\n\n\nPlease enter a name for your kingdom!")

    confirm_species = False
    while not confirm_species:
        print("\n\n\n" + get.species_list("list_all"))

        selected_species = input("Enter the species name for more information: ").strip().lower()
        if selected_species in get.species_list().keys():
            print("\n\n\n"
                  "==========\n" +
                  get.species_list(selected_species)["name"].upper() + "\n"
                  "\n" +
                  get.species_list(selected_species)["desc"] +
                  "==========\n")
            while True:
                confirm = input("Do you want to be a " + selected_species.upper() + "? (y/n): ").strip().lower()
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
        print("\n\n\n" + get.class_list("list_all"))

        selected_class = input("Enter the class name for more information: ").strip().lower()
        if selected_class in get.class_list().keys():
            print("\n\n\n"
                  "==========\n" +
                  selected_class.upper() + "\n"
                  "\n" +
                  get.class_list(selected_class)["desc"] +
                  "==========\n")
            while True:
                confirm = input("Do you want to be a " + selected_class.upper() + "? (y/n): ").strip().lower()
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
        confirm = input("Is this the character you want to create? (y/n): ").strip().lower()
        if confirm == "y":
            return new_character
        elif confirm == "n":
            character()
        else:
            print("\n\n\nPlease confirm your character information.")


def big_bad_evil_guy():
    """
    Ask player to name the BBEG.

    :postcondition: prompt the player to pick a name for the BBEG
    :return: the dictionary containing the BBEG's enemy information

    >>> big_bad_evil_guy()
    {}
    """
    unnamed_big_bad_evil_guy = {"name": "",
                                "max_HP": 0,
                                "current_HP": 0,
                                "max_SP": 0,
                                "current_SP": 0,
                                "ATK": 0,
                                "DEF": 0,
                                "AGI": 0,
                                "LUK": 0}

    while True:
        bbeg_name = input("\n\n\nWhat is the name of the usurper?: ").strip()
        if bbeg_name != "":
            unnamed_big_bad_evil_guy["name"] = bbeg_name
            return unnamed_big_bad_evil_guy
        else:
            print("\n\n\nPlease enter a name for your enemy!")


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
