"""

Kanon Nishiyama
A1415217

"""


from random import randint

from colorama import Style, Fore

from modules import display


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
        validate_movement(player_input, character, board)
    elif player_input == "help":
        pass
    else:
        print(f"\n\n\n{Style.BRIGHT}Invalid command.{Style.RESET_ALL}\n\n\n")


def validate_movement(direction, character, board):
    """
    Check if move is valid.

    :param direction: a string
    :param character: is a dictionary
    :param board: is a dictionary
    :precondition: direction must be a valid input given by validate_exploration_command()
    :precondition: character must be a dictionary from get.blank_character function
    :precondition: board must be a dictionary from get.tutorial_board or get.main_board function
    :postcondition: compare the current locations coordinates to the character coodinates to see if
                    movement in direction is valid
    :postcondition: if movement is valid, move the player coordinates according to the direction

    >>> current_board = {(0, 0): 'Empty room'}
    >>> current_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> chosen_direction = "w"
    >>> validate_movement(direction, character, board)
    False
    >>> current_board = {(0, 0): "Empty room", (0, 1): "Empty room", (1, 0): "Empty room", (1, 1): "Empty room"}
    >>> current_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> chosen_direction = "s"
    >>> validate_movement(direction, character, board)
    True
    """
    current_character_coordinate = (character["x-coordinate"], character["y-coordinate"])
    print(current_character_coordinate)
    current_location_walls = board[current_character_coordinate]["walls"]
    print(current_location_walls)

    if direction not in current_location_walls:
        move_character(direction, character)
    else:
        print(f"\n\n\n{Style.BRIGHT}You can't move that way.{Style.RESET_ALL}\n\n\n")


def move_character(direction, character):
    """
    Move the characters in the direction.

    :param direction: string
    :param character: a dictionary
    :precondition: direction must be a valid input given by the validate_movement function
    :precondition: character must be a dictionary from get.blank_character function
    :postcondition: adjust character coordinates in the given direction

    >>> current_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> move_character("s", current_character)
    >>> print(current_character)
    {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
    >>> current_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> move_character("d", current_character)
    >>> print(current_character)
    {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
    """
    if direction == "n":
        character["y-coordinate"] -= 1
    elif direction == "s":
        character["y-coordinate"] += 1
    elif direction == "e":
        character["x-coordinate"] += 1
    elif direction == "w":
        character["x-coordinate"] -= 1


def if_alive(character):
    if character["current_HP"] <= 0:
        return False
    else:
        return True


def enemy_encounter(character, board):
    current_coordinate = (character["x-coordinate"], character["y-coordinate"])
    area_type = board[current_coordinate]["area"]

    chance = 1

    if area_type == "safe":
        return False
    elif area_type == "field" or area_type == "dungeon":
        chance = 5
    elif area_type == "forest":
        chance = 2

    result = randint(1, chance)

    if result == chance:
        print(f"\n\n\n{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}+++ You encountered an enemy! +++{Style.RESET_ALL}\n\n\n")
        return True
    else:
        return False


def level_up(character):
    if character["EXP"] <= 0:
        exp_for_next_level = 50 * (character["LVL"] - 1)

        character["LVL"] += 1
        character["EXP"] += exp_for_next_level
        character["current_HP"] += 5 * (character["LVL"] - 1)
        character["max_HP"] += 5 * (character["LVL"] - 1)
        character["current_SP"] += 2 * (character["LVL"] - 1)
        character["max_SP"] += 2 * (character["LVL"] - 1)
        character["ATK"] += 5
        character["DEF"] += 5
        character["AGI"] += 5
        character["LUK"] += 2

        print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}+++ LEVEL UP! +++{Style.RESET_ALL}")


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
