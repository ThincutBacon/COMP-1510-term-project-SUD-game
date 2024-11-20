"""

Kanon Nishiyama
A1415217

"""
from pprint import pprint

from modules import create_character, get


def game():
    """
    Drive the game.
    """
    player_character = {}
    bbeg = {}

    confirm_create = False
    while not confirm_create:
        player_character = get.blank_character()
        print("\n\n")
        create_character.name_kingdom(player_character)
        print("\n\n")
        create_character.name_character(player_character)
        print("\n\n")
        create_character.choose_species(player_character)
        print("\n\n")
        create_character.choose_class(player_character)
        print("\n\n")
        confirm_create = create_character.confirm_character(player_character)

    confirm_create = False
    while not confirm_create:
        bbeg = get.unnamed_bbeg()
        print("\n\n")
        create_character.name_bbeg(bbeg)
        confirm_create = create_character.confirm_bbeg_name(bbeg)

    pprint(player_character)
    pprint(bbeg)


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
