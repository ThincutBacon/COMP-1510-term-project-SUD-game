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
    character_level = f"LVL {format(character['LVL'], '2')}"
    character_exp = f"EXP until LVL up: {format(character['EXP'], '4')}"

    sp_discount = 0
    if character['species'] == "elf":
        sp_discount = 1
    equipment_bonus = 0
    if character['species'] == "dwarf":
        equipment_bonus = 1

    skill_list = get.class_list(character['skill_class'])['skill_list']
    first_skill = (f"{format(skill_list[0].title(), '15')}: "
                   f"{format(get.skill_list(skill_list[0])["cost"] - sp_discount, '3')} SP ")
    second_skill = (f"{format(skill_list[1].title(), '15')}: "
                    f"{format(get.skill_list(skill_list[1])["cost"] - sp_discount, '3')} SP ")
    third_skill = (f"{format(skill_list[2].title(), '15')}: "
                   f"{format(get.skill_list(skill_list[2])["cost"] - sp_discount, '3')} SP ")

    hp = f"HP: {format(character['current_HP'], '3')} / {format(character['max_HP'], '3')}"
    sp = f"SP: {format(character['current_SP'], '3')} / {format(character['max_SP'], '3')}"

    atk_attribute = f"ATK: {format(character['ATK'], '3')}"
    def_attribute = f"DEF: {format(character['DEF'], '3')}"
    agi_attribute = f"AGI: {format(character['AGI'], '3')}"
    luk_attribute = f"LUK: {format(character['LUK'], '3')}"

    weapon_name = character['equipment']['weapon']
    armour_name = character['equipment']['armour']

    weapon_display = (f"{format("WEAPON", '7')}: {format(weapon_name.title(), '28')}{Fore.MAGENTA}[+"
                      f"{format(get.shop_information("weapon")[weapon_name]["modifier"] + equipment_bonus, '2')}"
                      f"]{Fore.RESET}")
    armour_display = (f"{format("ARMOUR", '7')}: {format(armour_name.title(), '28')}{Fore.BLUE}[+"
                      f"{format(get.shop_information("armour")[armour_name]["modifier"] + equipment_bonus, '2')}"
                      f"]{Fore.RESET}")

    print(f"==============================================\n"
          f"| {Style.BRIGHT}{format(character_name, '42')}{Style.RESET_ALL} |\n"
          f"| {format(class_and_species, '42')} |\n"
          f"| {format(kingdom_name, '42')} |\n"
          f"| {format("", '42')} |\n"
          f"| {Style.BRIGHT}{format(character_level, '15')}{Style.RESET_ALL}  {Style.BRIGHT}"
          f"{format(character_exp, '25')}{Style.RESET_ALL} |\n"
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
          f"|--------------------------------------------|\n"
          f"| {Style.BRIGHT}{format("EQUIPMENT", '42')}{Style.RESET_ALL} |\n"
          f"| {format("=============", '42')} |\n"
          f"| {format(weapon_display, '42')} |\n"
          f"| {format(armour_display, '42')} |\n"
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


def battle_status(character, enemy, round_count):
    enemy_name = f"{enemy['name'].upper()}"
    enemy_hp = f"HP: {format(enemy['current_HP'], '3')} / {format(enemy['max_HP'], '3')}"
    enemy_dialogue = "\"TESTING\""

    character_name = f"{character['name'].upper()}"
    character_hp = f"HP: {format(character['current_HP'], '3')} / {format(character['max_HP'], '3')}"
    character_sp = f"SP: {format(character['current_SP'], '3')} / {format(character['max_SP'], '3')}"

    print(f"ROUND {round_count}\n"
          f"==============================================\n"
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

    if character_inventory != {}:
        for item in character_inventory.keys():
            single_item = f"{format(item.title(), '20')}:  {format(character_inventory[item], '3')}"
            inventory_display += f"| {format(single_item, '26')} |\n"
    elif character_inventory == {}:
        inventory_display += (f"| {format("", '26')} |\n"
                              f"| {format("  No items in inventory.", '26')} |\n"
                              f"| {format("", '26')} |\n")
    else:
        print("ERROR")

    inventory_display += "==============================\n"

    print(inventory_display)


def shop_wares(option_list):
    """
    Print character information.

    :param character: a dictionary
    :precondition: character must be a dictionary from get.blank_character function
    :postcondition: print character information for the player to easily read

    >>> character_info()
    ''
    """
    shop_display = (f"==================================================\n"
                    f"| {Style.BRIGHT}{format("WARES", '46')}{Style.RESET_ALL} |\n"
                    f"| {format("----------------------------------------------", '46')} |\n")

    count = 1
    for item in option_list["all_items"]:
        single_item = f"{count}. {format(item.title(), '30')}:  {format(option_list[item]["cost"], '4')} Gold"
        shop_display += f"| {format(single_item, '46')} |\n"
        count += 1

    shop_display += "==================================================\n"

    print(shop_display)


def ask_player_purchase(option_list):
    """
    Sentence.

    :param x: x
    :precondition: x
    :postcondition: x
    :return: x

    >>> function()
    ''
    """
    while True:
        player_input = input(f"{Fore.WHITE}{Style.BRIGHT}Player command (or Back): {Style.RESET_ALL}")
        if player_input == "back":
            return player_input
        try:
            return option_list[int(player_input) - 1]
        except ValueError:
            pass
        except IndexError:
            pass
        except TypeError:
            pass
        print(f"\n\n\n{Style.BRIGHT}Invalid input{Style.RESET_ALL}\n\n\n")


def purchase_item(character, purchased_item, shop_type):
    purchase_cost = get.shop_information(shop_type)[purchased_item]["cost"]

    if character["gold"] >= purchase_cost:
        if shop_type == "item":
            character["gold"] -= purchase_cost
            try:
                character["inventory"][purchased_item] += 1
            except KeyError:
                character["inventory"][purchased_item] = 1
        else:
            character["gold"] -= purchase_cost
            character["equipment"][shop_type] = purchased_item
            modifier = get.shop_information(shop_type)[purchased_item]["modifier"]

            if shop_type == "weapon":
                character["modifier"]["ATK"] = modifier
            elif shop_type == "armour":
                character["modifier"]["DEF"] = modifier


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
