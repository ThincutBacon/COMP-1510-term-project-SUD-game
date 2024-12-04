"""

Kanon Nishiyama
A1415217

"""


from modules import get

from colorama import Fore, Style


def character_info(character):
    """
    Print character information.

    :param character: a dictionary
    :precondition: character must be a dictionary from get.blank_character function
    :postcondition: print character information for the player to easily read

    >>> character_info()
    ''
    """
    character_name = f"{character['name'].upper()}"
    class_and_species = f"{character['species_adjective'].title()} {character['skill_class'].title()}"
    kingdom_name = f"Heir to the throne of {character['kingdom'].upper()}"

    skill_list = get.class_list(character['skill_class'])['skill_list']
    first_skill = f"{format(skill_list[0].title(), '15')}: 2323 SP "
    second_skill = f"{format(skill_list[1].title(), '15')}: 2323 SP "
    third_skill = f"{format(skill_list[2].title(), '15')}: 2323 SP "

    hp = f"HP: {format(character['current_HP'], '3')} / {format(character['max_HP'], '3')}"
    sp = f"SP: {format(character['current_SP'], '3')} / {format(character['max_SP'], '3')}"

    atk_attribute = f"ATK: {format(character['ATK'], '3')}"
    def_attribute = f"DEF: {format(character['DEF'], '3')}"
    agi_attribute = f"AGI: {format(character['AGI'], '3')}"
    luk_attribute = f"LUK: {format(character['LUK'], '3')}"

    print(f"==============================================\n"
          f"| {Style.BRIGHT}{format(character_name, '42')}{Style.RESET_ALL} |\n"
          f"| {format(class_and_species, '42')} |\n"
          f"| {format(kingdom_name, '42')} |\n"
          f"|--------------------------------------------|\n"
          f"| {Style.BRIGHT}{format("STATS", '20')}{Style.RESET_ALL}"
          f"| {Style.BRIGHT}{format("ATTRIBUTES", '20')}{Style.RESET_ALL} |\n"
          f"| {format("=============", '20')}| {format("=============", '20')} |\n"
          f"| {Fore.RED}{format(hp, '20')}{Fore.RESET}| {Fore.MAGENTA}{format(atk_attribute, '20')}{Fore.RESET} |\n"
          f"| {Fore.CYAN}{format(sp, '20')}{Fore.RESET}| {Fore.BLUE}{format(def_attribute, '20')}{Fore.RESET} |\n"
          f"| {format("", '20')}| {Fore.YELLOW}{format(agi_attribute, '20')}{Fore.RESET} |\n"
          f"| {format("", '20')}| {Fore.GREEN}{format(luk_attribute, '20')}{Fore.RESET} |\n"
          f"|--------------------------------------------|\n"
          f"| {Style.BRIGHT}{format("SKILLS", '42')}{Style.RESET_ALL} |\n"
          f"| {format("=============", '42')} |\n"
          f"| {format(first_skill, '42')} |\n"
          f"| {format(second_skill, '42')} |\n"
          f"| {format(third_skill, '42')} |\n"
          f"==============================================\n")


def current_map(character, board):
    """
    Display a map and the players current location.

    :param character: is a dictionary
    :param board: is a dictionary
    :precondition: character must be a dictionary from get.blank_character function
    :precondition: board must be a dictionary from get.tutorial_board or get.main_board function
    :postcondition: print map with current location informtion for the player to easily read

    >>> character_info()
    ''
    """
    max_x_coordinate = sorted(board.keys())[-1][0]
    max_y_coordinate = sorted(board.keys())[-1][1]

    current_coordinates = (character['x-coordinate'], character['y-coordinate'])
    current_location_info = board[current_coordinates]

    full_map = ""

    for col in range(0, max_y_coordinate + 1):
        square_walls = board[(0, col)]['walls']
        if "n" in square_walls:
            full_map += f" --- "
        else:
            full_map += "     "
    full_map += "\n"
    for row in range(0, max_x_coordinate + 1):
        for layer in range(0, 2):
            for col in range(0, max_y_coordinate + 1):
                square_walls = board[(row, col)]['walls']
                if layer == 0:
                    w_wall = ""
                    e_wall = ""
                    if "w" in square_walls:
                        w_wall = "|"
                    elif "e" in square_walls:
                        e_wall = "|"

                    player_left = ""
                    player_right = ""
                    if (row, col) == current_coordinates:
                        player_left = f"{Fore.LIGHTCYAN_EX}{"{"}{Fore.RESET}"
                        player_right = f"{Fore.LIGHTCYAN_EX}{"}"}{Fore.RESET}"

                    map_symbol = "·"
                    try:
                        area_symbol = board[(row, col)]['symbol']
                        if area_symbol == "shop":
                            map_symbol = f"{Fore.LIGHTYELLOW_EX}${Fore.RESET}"
                        elif area_symbol == "exit":
                            map_symbol = f"{Fore.LIGHTGREEN_EX}?{Fore.RESET}"
                        elif area_symbol == "danger":
                            map_symbol = f"{Fore.LIGHTRED_EX}*{Fore.RESET}"
                    except KeyError:
                        pass

                    full_map += (f"{format(w_wall, '1')}"
                                 f"{format(player_left, '1')}"
                                 f"{format(map_symbol, '1')}"
                                 f"{format(player_right, '1')}"
                                 f"{format(e_wall, '1')}")

                if layer == 1:
                    s_wall = ""
                    if "s" in square_walls:
                        s_wall = "---"
                    full_map += f" {format(s_wall, '3')} "
            full_map += "\n"

    unmovable_directions = current_location_info['walls']
    movable_directions = "Exits: "
    if "n" not in unmovable_directions:
        movable_directions += "N "
    if "w" not in unmovable_directions:
        movable_directions += "W "
    if "e" not in unmovable_directions:
        movable_directions += "E "
    if "s" not in unmovable_directions:
        movable_directions += "S "

    print(f"{Style.BRIGHT}{current_location_info['name']}{Style.RESET_ALL}\n"
          f"{full_map}"
          f"{movable_directions}")


def location_desc(character, board):
    current_coordinates = (character['x-coordinate'], character['y-coordinate'])
    description = board[current_coordinates]["look"]
    print(f"{Fore.WHITE}================================================================={Fore.RESET}\n"
          f"\n"
          f"{Style.BRIGHT}You look around:{Style.RESET_ALL}\n"
          f"\n"
          f"{description}"
          f"\n"
          f"{Fore.WHITE}================================================================={Fore.RESET}\n")


def battle_status(character, enemy):
    enemy_name = f"{enemy['name'].upper()}"
    enemy_hp = f"HP: {format(enemy['current_HP'], '3')} / {format(enemy['max_HP'], '3')}"
    enemy_dialogue = "\"TESTING\""

    character_name = f"{character['name'].upper()}"
    character_hp = f"HP: {format(character['current_HP'], '3')} / {format(character['max_HP'], '3')}"
    character_sp = f"SP: {format(character['current_SP'], '3')} / {format(character['max_SP'], '3')}"

    print(f"==============================================\n"
          f"| {Style.BRIGHT}{format(enemy_name, '42')}{Style.RESET_ALL} |\n"
          f"| {Fore.RED}{format(enemy_hp, '42')}{Fore.RESET} |\n"
          f"| {Fore.WHITE}{format(enemy_dialogue, '42')}{Fore.RESET} |\n"
          f"|--------------------------------------------|\n"
          f"| {Style.BRIGHT}{format(character_name, '42')}{Style.RESET_ALL} |\n"
          f"| {Fore.RED}{format(character_hp, '20')}{Fore.RESET}"
          f"| {Fore.MAGENTA}{format(character_sp, '20')}{Fore.RESET} |\n"
          f"==============================================\n")


def inventory(character):
    """
    Print character information.

    :param character: a dictionary
    :precondition: character must be a dictionary from get.blank_character function
    :postcondition: print character information for the player to easily read

    >>> character_info()
    ''
    """
    character_inventory = character["inventory"]

    inventory_display = (f"==============================\n"
                         f"| {Style.BRIGHT}{format("INVENTORY", '26')}{Style.RESET_ALL} |\n"
                         f"| {format("--------------------------", '26')} |\n")


    for item in character_inventory.keys():
        single_item = f"{format(item.title(), '20')}:  {format(character_inventory[item], '3')}"
        inventory_display += f"| {format(single_item, '26')} |\n"

    inventory_display += "==============================\n"

    print(inventory_display)


def main():
    """
    Drive the program.
    """
    character = get.blank_character()
    character["inventory"] = {"Rabbit Horn": 999, "asd": 2, "DWE": 5, "sda": 1, "hfd": 7, "sdfsdfsfsfs": 2, "df": 1, }

    inventory(character)


if __name__ == "__main__":
    main()
