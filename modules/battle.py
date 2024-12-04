"""

Kanon Nishiyama
A1415217

"""
import math
from random import randint

from colorama import Fore, Style


def ask_player_input(option_list):
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
        count = 1
        display_options = ""
        for option in option_list:
            display_options += f"{count}. {option.upper()}\n"
            count += 1

        print(display_options)
        player_input = input(f"{Fore.WHITE}{Style.BRIGHT}Player command: {Style.RESET_ALL}")
        try:
            return option_list[int(player_input) - 1]
        except ValueError or IndexError or TypeError:
            print(f"\n\n\n{Style.BRIGHT}Invalid input{Style.RESET_ALL}\n\n\n")


def attack(attacker, receiver):
    """
    Sentence.

    :param x: x
    :precondition: x
    :postcondition: x
    :return: x

    >>> attack(attacker, receiver)
    ''
    """
    attacker_atk = (attacker["ATK"] +
                    attacker["buff"]["ATK"]["effect"] +
                    attacker["debuff"]["ATK"]["effect"] +
                    attacker["modifiers"]["ATK"])
    attacker_def = (attacker["DEF"] +
                    attacker["buff"]["DEF"]["effect"] +
                    attacker["debuff"]["DEF"]["effect"] +
                    attacker["modifiers"]["DEF"])
    attacker_luk = (attacker["LUK"] +
                    attacker["buff"]["LUK"]["effect"] +
                    attacker["debuff"]["LUK"]["effect"] +
                    attacker["modifiers"]["LUK"])

    attacker["reduce_damage"] = math.ceil(attacker_def // 4)

    attacker_damage = math.ceil(attacker_atk // 4)
    crit_chance = round(randint(1, 20) * (1 + (attacker_luk/100)))

    if crit_chance >= 20:
        print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}CRITICAL!!{Style.RESET_ALL}")
        attacker_damage *= 2

    print(attacker_damage)

    total_damage = receiver["reduce_damage"] - attacker_damage
    print(total_damage)

    if total_damage > 0:
        total_damage = 0

    receiver["current_HP"] += total_damage


def defend(defender):
    """
    Sentence.

    :param x: x
    :precondition: x
    :postcondition: x
    :return: x

    >>> defend(defender)
    ''
    """
    defender_def = (defender["DEF"] +
                    defender["buff"]["DEF"]["effect"] +
                    defender["debuff"]["DEF"]["effect"] +
                    defender["modifiers"]["DEF"])

    defender["reduce_damage"] = math.floor(defender_def // 2)


def skill_usable(skill, user):
    """
    Sentence.

    :param x: x
    :precondition: x
    :postcondition: x
    :return: x

    >>> function()
    ''
    """
    cost_payable = True

    if skill == "shield":
        cost_payable = user["current_SP"] >= 1
    elif skill == "shield bash":
        cost_payable = user["current_SP"] >= 3
    elif skill == "battle cry":
        cost_payable = user["current_SP"] >= 2
    elif skill == "sharper edge":
        cost_payable = user["current_SP"] >= 2
    elif skill == "focus attack":
        cost_payable = user["current_SP"] >= 3
    elif skill == "haste":
        cost_payable = user["current_SP"] >= 1
    elif skill == "fireball":
        cost_payable = user["current_SP"] >= 3
    elif skill == "freezing touch":
        cost_payable = user["current_SP"] >= 2
    elif skill == "healing light":
        cost_payable = user["current_SP"] >= 3

    if not cost_payable:
        return False
    else:
        return True


def use_skill(skill, round_count, user, receiver):
    """
    Sentence.

    :param x: x
    :precondition: x
    :postcondition: x
    :return: x

    >>> function()
    ''
    """
    user_def = (user["DEF"] +
                user["buff"]["DEF"]["effect"] +
                user["debuff"]["DEF"]["effect"] +
                user["modifiers"]["DEF"])

    if skill == "shield":
        user["current_SP"] -= 1
        user["reduce_damage"] = user_def
    elif skill == "shield bash":
        user["current_SP"] -= 3
        defend(user)
        attack(user, receiver)
    elif skill == "battle cry":
        user["current_SP"] -= 2
        receiver["debuff"]["DEF"] = {"effect": -5, "time": round_count + 2}
    elif skill == "sharper edge":
        user["current_SP"] -= 2
        user["buff"]["ATK"] = {"effect": 5, "time": round_count + 2}
    elif skill == "focus attack":
        user["current_SP"] -= 3
        user["buff"]["LUK"] = {"effect": 5, "time": round_count + 2}
        attack(user, receiver)
    elif skill == "haste":
        user["current_SP"] -= 1
        user["buff"]["AGI"] = {"effect": 5, "time": round_count + 2}
    elif skill == "fireball":
        user["current_SP"] -= 3
        user["continuous_damage"] = {"effect": 5, "time": round_count + 2}
    elif skill == "freezing touch":
        user["current_SP"] -= 2
        receiver["debuff"]["AGI"] = {"effect": -5, "time": round_count + 2}
    elif skill == "healing light":
        user["current_SP"] -= 3
        user["current_HP"] += 10
        if user["current_HP"] > user["max_HP"]:
            user["current_HP"] = user["max_HP"]


def skill_effect_time(character, round_count):
    all_buffs = character["buff"]
    all_debuffs = character["debuff"]

    for attribute in all_buffs.keys() and all_debuffs.keys():
        if attribute["time"] == round_count:
            all_buffs[attribute] = {"effect": 0, "time": 0}

    if character["continuous_damage"]["time"] == round_count:
        character["continuous_damage"] = {"effect": 0, "time": 0}


def use_item(item, user):
    """
    Sentence.

    :param x: x
    :precondition: x
    :postcondition: x
    :return: x

    >>> function()
    ''
    """
    if item == "healing potion (s)":
        user["inventory"][item] -= 1
        user["current_HP"] += 5
        if user["current_HP"] > user["max_HP"]:
            user["current_HP"] = user["max_HP"]
    elif item == "healing potion (m)":
        user["inventory"][item] -= 1
        user["current_HP"] += 10
        if user["current_HP"] > user["max_HP"]:
            user["current_HP"] = user["max_HP"]
    elif item == "healing potion (l)":
        user["inventory"][item] -= 1
        user["current_HP"] += 20
        if user["current_HP"] > user["max_HP"]:
            user["current_HP"] = user["max_HP"]
    elif item == "energy potion (s)":
        user["inventory"][item] -= 1
        user["current_SP"] += 3
        if user["current_SP"] > user["max_SP"]:
            user["current_SP"] = user["max_SP"]
    elif item == "energy potion (m)":
        user["inventory"][item] -= 1
        user["current_SP"] += 5
        if user["current_SP"] > user["max_SP"]:
            user["current_SP"] = user["max_SP"]
    elif item == "energy potion (l)":
        user["inventory"][item] -= 1
        user["current_SP"] += 10
        if user["current_SP"] > user["max_SP"]:
            user["current_SP"] = user["max_SP"]

    for item in user["inventory"].keys():
        if user["inventory"][item] <= 0:
            user["inventory"].pop(item)



def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
