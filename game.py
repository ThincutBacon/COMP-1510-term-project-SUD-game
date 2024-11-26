"""

Kanon Nishiyama
A1415217

"""
from pprint import pprint

from modules import create_character, get


def create_new_character(character, bbeg):
    """
    Drive the character creation.
    """
    confirm_create = False
    while not confirm_create:
        print("\n\n")
        create_character.name_kingdom(character)
        print("\n\n")
        create_character.name_character(character)
        print("\n\n")
        create_character.choose_species(character)
        print("\n\n")
        create_character.choose_class(character)
        print("\n\n")
        confirm_create = create_character.confirm_character(character)

    confirm_create = False
    while not confirm_create:
        print("\n\n")
        create_character.name_bbeg(bbeg)
        confirm_create = create_character.confirm_bbeg_name(bbeg)


def game():
    """
    Drive the game.
    """
    player_character = get.blank_character()
    bbeg = get.unnamed_bbeg()

    create_new_character(player_character, bbeg)

    pprint(player_character)
    pprint(bbeg)


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
