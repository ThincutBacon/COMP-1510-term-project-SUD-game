"""

Kanon Nishiyama
A1415217

"""
from modules import get


def name_kingdom(character):
    """
    Ask the player to name their kingdom.

    :param character: a dictionary
    :precondition: character must be a dictionary from get.blank_character function
    :postcondition: change the value of key "kingdom" to player input

    >>> test_character = get.blank_character()
    >>> name_kingdom(test_character)
    ''
    """
    while True:
        kingdom_name = input("\n\n\nWhat is the name of your kingdom?: ").strip()
        if kingdom_name != "":
            character["kingdom"] = kingdom_name
            break
        else:
            print("\n\n\nPlease enter a name for your kingdom!")


def name_character(character):
    """
    Ask the player to name their character.

    :param character: a dictionary
    :precondition: character must be a dictionary from get.blank_character function
    :postcondition: change the value of key "name" to player input

    >>> test_character = get.blank_character()
    >>> name_character(test_character)
    ''
    """
    while True:
        print("\n\n\nAs heir to the throne of " + character["kingdom"].upper() + ",")
        character_name = input("What is your name?: ").strip()
        if character_name != "":
            character["name"] = character_name
            break
        else:
            print("\n\n\nPlease enter a name for your kingdom!")


def choose_species(character):
    """
    Ask the player to choose their character's species.

    :param character: a dictionary
    :precondition: character must be a dictionary from get.blank_character function
    :postcondition: change the value of key "species" to player input
    :postcondition: change the values of character attributes based on chosen species

    >>> test_character = get.blank_character()
    >>> choose_species(test_character)
    ''
    """
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
                    character["species"] = selected_species
                    confirm_species = True
                    break
                elif confirm == "n":
                    break
                else:
                    print("\n\n\nPlease confirm your selection.\n\n\n")
        else:
            print("\n\n\nPlease enter a valid species!")


def choose_class(character):
    """
    Ask the player to choose their character's class.

    :param character: a dictionary
    :precondition: character must be a dictionary from get.blank_character function
    :postcondition: change the value of key "class" to player input

    >>> test_character = get.blank_character()
    >>> choose_species(test_character)
    ''
    """
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
                    character["skill_class"] = selected_class
                    confirm_class = True
                    break
                elif confirm == "n":
                    break
                else:
                    print("\n\n\nPlease confirm your selection.\n\n\n")
        else:
            print("\n\n\nPlease enter a valid class!")


def confirm_character(character):
    """
    Ask player to confirm their character information.

    :param character: a dictionary
    :precondition: character must be a dictionary from get.blank_character function
    :postcondition: prompt the player to confirm their character
    :return: if the player confirms their character, return True
    :return: if the player denies their character, return False

    >>> test_character = get.blank_character()
    >>> confirm_character(test_character)
    {}
    """
    confirm_new_character = False
    while not confirm_new_character:
        print("\n\n\n"
              "==========\n"
              "Kingdom: " + character["kingdom"] + "\n"
              "Name: " + character["name"] + "\n"
              "\n"
              "Species: " + character["species"].title() + "\n"
              "Class: " + character["skill_class"].title() + "\n"
              "==========\n")
        confirm = input("Is this the character you want to create? (y/n): ").strip().lower()
        if confirm == "y":
            return True
        elif confirm == "n":
            return False
        else:
            print("\n\n\nPlease confirm your character information.")


def name_bbeg(bbeg):
    """
    Ask the player to name their kingdom.

    :param bbeg: a dictionary
    :precondition: bbeg must be a dictionary from get.unnamed_bbeg function
    :postcondition: change the value of key "name" to player input

    >>> test_bbeg = get.unnamed_bbeg()
    >>> name_bbeg(test_bbeg)
    ''
    """
    while True:
        print("Before you embark, remind me,")
        bbeg_name = input("\n\n\nWhat is the name of your usurper?: ").strip()
        if bbeg_name != "":
            bbeg["name"] = bbeg_name
            break
        else:
            print("\n\n\nPlease enter a name for your enemy!")


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
