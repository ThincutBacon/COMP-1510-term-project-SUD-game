"""

Kanon Nishiyama
A1415217

"""

from colorama import Style
from modules import display, get


def validate_exploration_command(player_input, character, board):
    """
    Check if the player command is valid and run the corresponding function.

    :param player_input: a string
    :param character: is a dictionary
    :param board: is a dictionary
    :precondition: player_input must be a string
    :precondition: character must be a dictionary from get.blank_character function
    :precondition: board must be a dictionary from get.tutorial_board or get.main_board function
    :postcondition: run a function if the player_input matches the set command name

    >>> validate_exploration_command()
    ''
    """
    if player_input == "look":
        display.location_desc(character, board)
    elif player_input == "stat":
        display.character_info(character)
    elif player_input == "map":
        display.current_map(character, board)
    elif player_input == "n" or player_input == "e" or player_input == "s" or player_input == "w":
        pass
    elif player_input == "help":
        pass
    else:
        print(f"\n\n\n{Style.BRIGHT}Invalid command.{Style.RESET_ALL}\n\n\n")





def main():
    """
    Drive the program.
    """
    character = get.blank_character()
    character["name"] = "OAIhsdoaihsdoasdssssssssssssssssssssssssss"
    character["kingdom"] = "Heilia"
    character["species_adjective"] = "elven"
    character["skill_class"] = "mage"
    character['x-coordinate'] = 1
    character['y-coordinate'] = 1

    player_input = input("Enter a player command: ").strip().lower()
    validate_exploration_command(player_input, character, get.main_board())


if __name__ == "__main__":
    main()
