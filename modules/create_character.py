"""

Kanon Nishiyama
A1415217

"""
from pprint import pprint
from modules import get


def name_kingdom(character):
    """
    Ask the player to name their kingdom.

    :param character: a dictionary
    :precondition: character must be a dictionary from get.blank_character function
    :postcondition: change the value of key "kingdom" to player input

    >>> test_character = get.blank_character() #doctest: +SKIP
    >>> name_kingdom(test_character) #doctest: +SKIP
    What is the name of your kingdom?:
    >>> player_input = "Hyrule" #doctest: +SKIP
    >>> print(test_character["kingdom"]) #doctest: +SKIP
    Hyrule
    """
    while True:
        kingdom_name = input("What is the name of your kingdom?: ").strip()
        if kingdom_name != "":
            character["kingdom"] = kingdom_name
            break
        else:
            print("\n\n\nPlease enter a name for your kingdom!\n\n\n")


def name_character(character):
    """
    Ask the player to name their character.

    :param character: a dictionary
    :precondition: character must be a dictionary from get.blank_character function
    :postcondition: change the value of key "name" to player input

    >>> test_character = get.blank_character() #doctest: +SKIP
    >>> test_character["kingdom"] = "Hyrule" #doctest: +SKIP
    >>> name_character(test_character) #doctest: +SKIP
    As heir to the throne of HYRULE,
    What is your name?:
    >>> player_input = "Zelda" #doctest: +SKIP
    >>> print(test_character["name"]) #doctest: +SKIP
    Zelda
    """
    while True:
        print("As heir to the throne of " + character["kingdom"].upper() + ",")
        character_name = input("What is your name?: ").strip()
        if character_name != "":
            character["name"] = character_name
            break
        else:
            print("\n\n\nPlease enter a name for your kingdom!\n\n\n")


def choose_species(character):
    """
    Ask the player to choose their character's species.

    :param character: a dictionary
    :precondition: character must be a dictionary from get.blank_character function
    :postcondition: change the value of key "species" to player input
    :postcondition: change the values of character attributes based on chosen species

    >>> test_character = get.blank_character() #doctest: +SKIP
    >>> choose_species(test_character) #doctest: +SKIP
    ==========
    HUMAN
    "The most versatile of species."

    ELF
    "The graceful guardians of the forests."

    DWARF
    "Inhabitants of the deepest caves and the highest mountains."
    ==========

    Enter the species name for more information:
    >>> player_input = "human" #doctest: +SKIP



    ==========
    HUMAN

    Although average in most aspects, they possess strong survival
    prowess and the ability to utilize items to their fullest potential.

    Highest Attributes: ATK and LUK
    Species Bonus: All items gain an additional +2 to their effects
    ==========

    Do you want to be a HUMAN? (y/n):
    >>> player_input = "y" #doctest: +SKIP
    >>> print(test_character["species"]) #doctest: +SKIP
    human
    """
    confirm_species = False
    while not confirm_species:
        print(get.species_list("list_all"))

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
                    print("\n\n")
                    break
                else:
                    print("\n\n\nPlease confirm your selection.\n\n\n")
        else:
            print("\n\n\nPlease enter a valid species!\n\n\n")


def choose_class(character):
    """
    Ask the player to choose their character's class.

    :param character: a dictionary
    :precondition: character must be a dictionary from get.blank_character function
    :postcondition: change the value of key "class" to player input

    >>> test_character = get.blank_character() #doctest: +SKIP
    >>> choose_species(test_character) #doctest: +SKIP
    ==========
    WARRIOR
    "For those who fight with endurance."

    SCOUT
    "For those who fight with deadly accuracy."

    MAGE
    "For those who fight by leveling the playing field."
    ==========

    Enter the class name for more information:
    >>> player_input = "scout" #doctest: +SKIP



    ==========
    SCOUT

    Scout's fight quick battles, inflicting fatal damage before their
    enemies have a chance to hurt them back.

    Class Skills:
    Sharper Edge - Increases your ATK
    Focus Attack - Attacks while increasing your LUK
    Haste - Increases your AGI
    ==========

    Do you want to be a SCOUT? (y/n):
    >>> player_input = "y" #doctest: +SKIP
    >>> print(test_character["skill_class"]) #doctest: +SKIP
    scout
    """
    confirm_class = False
    while not confirm_class:
        print(get.class_list("list_all"))

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
                    print("\n\n")
                    break
                else:
                    print("\n\n\nPlease confirm your selection.\n\n\n")
        else:
            print("\n\n\nPlease enter a valid class!\n\n\n")


def confirm_character(character):
    """
    Ask player to confirm their character information.

    :param character: a dictionary
    :precondition: character must be a dictionary from get.blank_character function
    :postcondition: prompt the player to confirm their character
    :return: if the player confirms their character, return True
    :return: if the player denies their character, return False

    >>> test_character = get.blank_character() #doctest: +SKIP
    >>> test_character["kingdom"] = "Hyrule" #doctest: +SKIP
    >>> test_character["name"] = "Zelda" #doctest: +SKIP
    >>> test_character["species"] = "elf" #doctest: +SKIP
    >>> test_character["skill_class"] = "mage" #doctest: +SKIP
    >>> confirm_character(test_character) #doctest: +SKIP
    ==========
    Kingdom: Hyrule
    Name: Tohru

    Species: Elf
    Class: Mage
    ==========

    Is this the character you want to create? (y/n):
    >>> player_input = "y" #doctest: +SKIP
    True
    """
    confirm_new_character = False
    while not confirm_new_character:
        print("==========\n"
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
            print("\n\n")
            return False
        else:
            print("\n\n\nPlease confirm your character information.\n\n\n")


def name_bbeg(bbeg):
    """
    Ask the player to name their kingdom.

    :param bbeg: a dictionary
    :precondition: bbeg must be a dictionary from get.unnamed_bbeg function
    :postcondition: change the value of key "name" to player input

    >>> test_bbeg = get.unnamed_bbeg() #doctest: +SKIP
    >>> name_bbeg(test_bbeg) #doctest: +SKIP
    Before you embark, remind me,
    What is the name of your usurper?:
    >>> player_input = "Ganondorf" #doctest: +SKIP
    >>> print(test_bbeg["name"]) #doctest: +SKIP
    Ganondorf
    """
    while True:
        print("Before you embark, remind me,")
        bbeg_name = input("What is the name of your usurper?: ").strip()
        if bbeg_name != "":
            bbeg["name"] = bbeg_name
            break
        else:
            print("\n\n\nPlease enter a name for your enemy!\n\n\n")


def confirm_bbeg_name(bbeg):
    """
    Ask player to confirm the bbeg's name.

    :param bbeg: a dictionary
    :precondition: bbeg must be a dictionary from get.unnamed_bbeg function
    :postcondition: prompt the player to confirm their bbeg
    :return: if the player confirms their character, return True
    :return: if the player denies their character, return False

    >>> test_bbeg = get.unnamed_bbeg() #doctest: +SKIP
    >>> test_bbeg["name"] = "Ganondorf" #doctest: +SKIP
    Is GANONDORF the name you swear vengeance against? (y/n):
    >>> player_input = "y" #doctest: +SKIP
    True
    """
    confirm_new_character = False
    while not confirm_new_character:
        confirm = input(
            "\nIs " + bbeg["name"].upper() + " the name you swear vengeance against? (y/n): "
        ).strip().lower()
        if confirm == "y":
            return True
        elif confirm == "n":
            print("\n\n")
            return False
        else:
            print("\n\n\nPlease confirm your character information.\n\n\n")


def main():
    """
    Drive the program.
    """
    character = get.blank_character()
    confirm_create = False
    while not confirm_create:
        character = get.blank_character()
        print("\n\n")
        name_kingdom(character)
        print("\n\n")
        name_character(character)
        print("\n\n")
        choose_species(character)
        print("\n\n")
        choose_class(character)
        print("\n\n")
        confirm_create = confirm_character(character)
    pprint(character)

    bbeg = get.unnamed_bbeg()
    confirm_create = False
    while not confirm_create:
        bbeg = get.unnamed_bbeg()
        print("\n\n")
        name_bbeg(bbeg)
        confirm_create = confirm_bbeg_name(bbeg)
    pprint(bbeg)


if __name__ == "__main__":
    main()
