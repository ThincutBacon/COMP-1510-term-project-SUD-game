"""

Kanon Nishiyama
A1415217

"""


import math

from colorama import Style, Fore

from modules import create_character, get, display, check, battle


def create_new_character(character, bbeg):
    """
    Drive the character creation.
    """
    confirm_create = False
    while not confirm_create:
        print("\n\n"
              f"{Style.BRIGHT}===== CHARACTER CREATION ====={Style.RESET_ALL}\n")
        create_character.name_kingdom(character)
        print("\n\n\n\n\n")
        create_character.name_character(character)
        print("\n\n\n\n\n")
        create_character.choose_species(character)
        print("\n\n\n\n\n")
        create_character.choose_class(character)
        print("\n\n\n\n\n")
        confirm_create = create_character.confirm_character(character)

    confirm_create = False
    while not confirm_create:
        print("\n\n\n\n\n")
        create_character.name_bbeg(bbeg)
        confirm_create = create_character.confirm_bbeg_name(bbeg)


def tutorial(character, bbeg):
    """
    Drive the tutorial.
    """
    current_board = get.tutorial_board()
    print(f"\n\n"
          f"{Style.BRIGHT}===== TUTORIAL ====={Style.RESET_ALL}\n"
          f"\n"
          f"Currently, you find yourself trapped within {Fore.BLUE}The Dungeons{Fore.RESET} after \n"
          f"being thrown in here by the {Fore.RED}King's Advisor{Fore.RESET}.\n"
          f"\n"
          f"Before you are able to set out on your quest for justice and \n"
          f"vengeance, you must break out of {Fore.BLUE}The Dungeons{Fore.RESET}.\n"
          f"\n"
          f"Luckily, you were able to escape your cell without being caught, \n"
          f"and now the doorway to your freedom is just a step away.\n")
    input(f"{Fore.WHITE}{Style.BRIGHT}Press Enter to continue: {Style.RESET_ALL}")

    print(f"\n\n\n\n\n")
    display.current_map(character, current_board)
    print(f"\n"
          f"What you see here is a map of your surroundings.\n"
          f"\n"
          f"Above the map shows the name of your current location, while the \n"
          f"Exits section under the map show all possible directions your \n"
          f"character is able to move in.\n"
          f"\n"
          f"The curly braces in {Fore.LIGHTCYAN_EX}CYAN{Fore.RESET} symbolize your current location, \n"
          f"while the question mark in {Fore.LIGHTGREEN_EX}GREEN{Fore.RESET} symbolize any doorways \n"
          f"that exit to a new area.\n")
    input(f"{Fore.WHITE}{Style.BRIGHT}Press Enter to continue: {Style.RESET_ALL}")

    print(f"\n\n\n"
          f"\n\n\n"
          f"Later on, you will see dollar signs in {Fore.LIGHTYELLOW_EX}YELLOW{Fore.RESET} which symbolize \n"
          f"shops, or asterisks in {Fore.LIGHTRED_EX}RED{Fore.RESET} that symbolize more dangerous areas.\n"
          f"\n"
          f"Anytime you want to see the map again, enter \"map\" whenever \n"
          f"prompted for player commands.\n"
          f"\n"
          f"Let's try is out now!\n"
          f"Type in \"map\" to display the map.\n")
    while True:
        player_input = input(f"{Fore.WHITE}{Style.BRIGHT}Player command: {Style.RESET_ALL}")
        if player_input == "map":
            print(f"\n\n\n"
                  f"\n\n")
            check.validate_exploration_command(player_input, character, current_board)
            break
        else:
            print("\n\n\nPlease input \"map\" for the tutorial.\n\n\n")

    print(f"\n"
          f"Good job! Now let's continue you're escape!\n")
    input(f"{Fore.WHITE}{Style.BRIGHT}Press Enter to continue: {Style.RESET_ALL}")

    print(f"\n\n\n"
          f"\n\n\n"
          f"Before moving any further, you should try and LOOK around to take \n"
          f"stock of your surroundings and stay alert of any guards that may \n"
          f"be patrolling the area.\n"
          f"\n"
          f"Try entering the \"look\" command now!\n")
    while True:
        player_input = input(f"{Fore.WHITE}{Style.BRIGHT}Player command: {Style.RESET_ALL}")
        if player_input == "look":
            print(f"\n\n\n"
                  f"\n\n")
            check.validate_exploration_command(player_input, character, current_board)
            break
        else:
            print("\n\n\nPlease input \"look\" for the tutorial.\n\n\n")

    print(f"Nice!\n"
          f"\n"
          f"Looking gives you move information on your current location.\n"
          f"\n"
          f"I would recommend looking whenever you move to a new location, as \n"
          f"it can provide you with hints on what to do or where to go next.\n")
    input(f"{Fore.WHITE}{Style.BRIGHT}Press Enter to continue: {Style.RESET_ALL}")

    print(f"\n\n\n"
          f"\n\n\n"
          f"According to the information provided by looking, your exit is to the "
          f"{Fore.GREEN}{Style.BRIGHT}EAST{Style.RESET_ALL} of here\n"
          f"\n"
          f"To move your character, enter \"n\", \"s\", \"e\", or \"w\" to move in that direction.\n"
          f"\n"
          f"When you're ready enter \"e\" to move.\n")
    while True:
        player_input = input(f"{Fore.WHITE}{Style.BRIGHT}Player command: {Style.RESET_ALL}")
        if player_input == "e":
            print(f"\n\n\n"
                  f"\n\n")
            check.validate_exploration_command(player_input, character, current_board)
            break
        else:
            print("\n\n\nPlease input \"e\" for the tutorial.\n\n\n")

    tutorial_enemy = get.random_enemy(character, current_board)
    print(f"\n\n\n"
          f"\n\n\n"
          f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}+++ You encountered an enemy! +++{Style.RESET_ALL}\n"
          f"\n\n")

    display.battle_status(character, tutorial_enemy, "1")
    print(f"{Style.BRIGHT}1. ATTACK{Style.RESET_ALL}\n"
          f"{Style.BRIGHT}2. DEFEND{Style.RESET_ALL}\n"
          f"{Style.BRIGHT}3. SKILL{Style.RESET_ALL}\n"
          f"{Style.BRIGHT}4. ITEM{Style.RESET_ALL}\n"
          "\n\n"
          f"You just entered a battle with an enemy!\n"
          f"\n"
          f"Above shows both the status of your character as well as your enemy.\n"
          f"When either of your {Fore.RED}HPs (Hit points){Fore.RESET} hit 0, that will be the when \n"
          f"combat will end.\n")
    input(f"{Fore.WHITE}{Style.BRIGHT}Press Enter to continue: {Style.RESET_ALL}")

    print(f"\n\n\n")
    display.battle_status(character, tutorial_enemy, "1")
    print(f"{Style.BRIGHT}1. ATTACK{Style.RESET_ALL}\n"
          f"{Style.BRIGHT}2. DEFEND{Style.RESET_ALL}\n"
          f"{Style.BRIGHT}3. SKILL{Style.RESET_ALL}\n"
          f"{Style.BRIGHT}4. ITEM{Style.RESET_ALL}\n"
          "\n\n"
          f"During an encounter, you are able to either {Style.BRIGHT}ATTACK{Style.RESET_ALL} the enemy, "
          f"{Style.BRIGHT}DEFEND{Style.RESET_ALL} \n"
          f"yourself, use a {Style.BRIGHT}SKILL{Style.RESET_ALL}, or use an {Style.BRIGHT}ITEM{Style.RESET_ALL}.\n"
          f"\n"
          f"To select an action, enter the corresponding number.\n"
          f"\n"
          f"Let's try {Style.BRIGHT}ATTACKING{Style.RESET_ALL} the enemy!\n")
    while True:
        player_input = input(f"{Fore.WHITE}{Style.BRIGHT}Player command: {Style.RESET_ALL}")
        if player_input == "1":
            print(f"\n\n\n"
                  f"\n\n")
            battle.attack(character, tutorial_enemy)
            break
        else:
            print("\n\n\nPlease input \"1\" for the tutorial.\n\n\n")

    print(f"\n\n\n")
    display.battle_status(character, tutorial_enemy, "2")
    print(f"{Style.BRIGHT}1. ATTACK{Style.RESET_ALL}\n"
          f"{Style.BRIGHT}2. DEFEND{Style.RESET_ALL}\n"
          f"{Style.BRIGHT}3. SKILL{Style.RESET_ALL}\n"
          f"{Style.BRIGHT}4. ITEM{Style.RESET_ALL}\n"
          "\n\n"
          f"Attacking your enemy deals simple damage to your enemy.\n"
          f"\n"
          f"The amount of damage inflicted is calculated through a combination \n"
          f"of your {Fore.MAGENTA}ATK{Fore.RESET} and {Fore.GREEN}LUK{Fore.RESET} attributes, as "
          f"well as your enemies {Fore.BLUE}DEF{Fore.RESET} \n"
          f"attribute.\n"
          f"\n"
          f"Next lets try {Style.BRIGHT}DEFENDING{Style.RESET_ALL} yourself!\n")
    while True:
        player_input = input(f"{Fore.WHITE}{Style.BRIGHT}Player command: {Style.RESET_ALL}")
        if player_input == "2":
            print(f"\n\n\n"
                  f"\n\n")
            battle.defend(character)
            break
        else:
            print("\n\n\nPlease input \"2\" for the tutorial.\n\n\n")

    print(f"\n\n\n")
    display.battle_status(character, tutorial_enemy, "3")
    print(f"{Style.BRIGHT}1. ATTACK{Style.RESET_ALL}\n"
          f"{Style.BRIGHT}2. DEFEND{Style.RESET_ALL}\n"
          f"{Style.BRIGHT}3. SKILL{Style.RESET_ALL}\n"
          f"{Style.BRIGHT}4. ITEM{Style.RESET_ALL}\n"
          "\n\n"
          f"By defending, you protect yourself against your enemies next attack, \n"
          f"increasing the amount of damage you are able to negate.\n"
          f"\n"
          f"The amount of damage you can negate is calculated with your {Fore.BLUE}DEF{Fore.RESET} attribute.\n"
          f"\n"
          f"Next lets try using a {Style.BRIGHT}SKILL{Style.RESET_ALL} and try using any skill you like!\n")
    while True:
        player_input = input(f"{Fore.WHITE}{Style.BRIGHT}Player command: {Style.RESET_ALL}")
        if player_input == "3":
            print(f"\n\n\n"
                  f"\n\n")
            while True:
                sp_discount = 0
                if character["skill_class"] == "mage":
                    sp_discount = 1
                player_skill_list = get.class_list(character["skill_class"])["skill_list"]
                chosen_skill = battle.ask_player_input(player_skill_list)
                usable_skill = battle.skill_usable(chosen_skill, character, sp_discount)
                if usable_skill:
                    battle.use_skill(chosen_skill, "3", character, tutorial_enemy, sp_discount)
                    break
                else:
                    print("Not enough SP!")
            break
        else:
            print("\n\n\nPlease input \"3\" for the tutorial.\n\n\n")

    print(f"\n\n\n")
    display.battle_status(character, tutorial_enemy, "4")
    print(f"{Style.BRIGHT}1. ATTACK{Style.RESET_ALL}\n"
          f"{Style.BRIGHT}2. DEFEND{Style.RESET_ALL}\n"
          f"{Style.BRIGHT}3. SKILL{Style.RESET_ALL}\n"
          f"{Style.BRIGHT}4. ITEM{Style.RESET_ALL}\n"
          "\n\n"
          f"You just used a skill!\n"
          f"\n"
          f"Skills are unique to you're characters class.\n"
          f"Enter the \"skill\" command to learn more about your skills.\n"
          f"\n"
          f"Next, let's try using an {Style.BRIGHT}ITEM{Style.RESET_ALL}! For the purpose of this tutorial, I will \n"
          f"be providing you a Healing Potion (S) to try out.\n")
    character["inventory"]["healing potion (s)"] = 1
    while True:
        player_input = input(f"{Fore.WHITE}{Style.BRIGHT}Player command: {Style.RESET_ALL}")
        if player_input == "4":
            player_item_list = list(character["inventory"].keys())
            print("\n\n\n")
            display.inventory(character)
            if not player_item_list:
                print("\n\n\n"
                      f"{Style.BRIGHT}No items to chose from.{Style.RESET_ALL}"
                      "\n\n\n")
            else:
                effect_bonus = 0
                if character["species"] == "human":
                    effect_bonus = 2
                chosen_item = battle.ask_player_input(player_item_list)
                battle.use_item(chosen_item, character, effect_bonus)
                break
        else:
            print("\n\n\nPlease input \"4\" for the tutorial.\n\n\n")

    print(f"\n\n\n")
    display.battle_status(character, tutorial_enemy, "5")
    print(f"{Style.BRIGHT}1. ATTACK{Style.RESET_ALL}\n"
          f"{Style.BRIGHT}2. DEFEND{Style.RESET_ALL}\n"
          f"{Style.BRIGHT}3. SKILL{Style.RESET_ALL}\n"
          f"{Style.BRIGHT}4. ITEM{Style.RESET_ALL}\n"
          "\n\n"
          f"You just used a {Fore.RED}Healing Potion{Fore.RESET}.\n"
          f"\n"
          f"{Fore.RED}Healing Potions{Fore.RESET}, like the name suggests, heals you, increasing your "
          f"{Fore.RED}HP{Fore.RESET}.\n"
          f"Other then healing potions, you can also use {Fore.RED}Energy Potions{Fore.RESET}, which when \n"
          f"used recover your {Fore.RED}SP{Fore.RESET}.\n"
          f"\n"
          f"Potions increase their potency by size, going from S, M, to L.\n"
          f"\n"
          f"You can buy potions at {Fore.LIGHTYELLOW_EX}Item Shops{Fore.RESET}.\n")
    input(f"{Fore.WHITE}{Style.BRIGHT}Press Enter to continue: {Style.RESET_ALL}")

    print(f"\n\n\n"
          f"Now that you know the basics, try and defeat the guard on your own!\n")
    input(f"{Fore.WHITE}{Style.BRIGHT}Press Enter to continue: {Style.RESET_ALL}")

    run_battle(character, tutorial_enemy, 5)

    if check.if_alive(character):
        print(f"\n\n\n"
              f"{Style.BRIGHT}Congratulations! You successfully defeated the guard!{Style.RESET_ALL}\n"
              f"\n"
              f"You are able to obtain the key to the {Fore.GREEN}Dungeon Exit!{Fore.RESET}\n"
              f"\n"
              f"Along with some coins and the key, you are able to loot a crude looking \n"
              f"dagger from the corpse.\n"
              f"You gain a Crude Iron Dagger (ATK +2)!\n")
        equipment_bonus = 0
        if character["species"] == "dwarf":
            equipment_bonus = 1
        character["equipment"]["weapon"] = "crude iron dagger"
        character["modifiers"]["ATK"] = 2 + equipment_bonus
        input(f"{Fore.WHITE}{Style.BRIGHT}Press Enter to continue: {Style.RESET_ALL}")

        print(f"\n\n\n"
              f"As you saw, when defeating enemies, they tend to drop a bit of gold, as well as \n"
              f"giving you some EXP.\n"
              f"\n"
              f"Gold can be used at shops, either to buy items or upgrade.\n"
              f"\n"
              f"EXP, when accumulated enough, allows you to LEVEL UP, boosting your base attributes.\n")

    elif not check.if_alive(character):
        print(f"\n\n\n"
              f"Oh. Well. That was unexpected.\n"
              f"\n"
              f"Since this is a tutorial, you aren't dead! I'll make sure to heal you up to "
              f"{Fore.RED}15 HP{Fore.RESET}.\n"
              f"\n"
              f"The guard you were fighting flees from combat!\n"
              f"In his fear, he seems to have dropped the key for the {Fore.GREEN}Dungeon Exit{Fore.RESET}. Hurray?\n")
        input(f"{Fore.WHITE}{Style.BRIGHT}Press Enter to continue: {Style.RESET_ALL}")

        print(f"\n\n\n"
              f"Normally, if you are able to defeat an enemy, they tend to drop a bit of gold, as well as \n"
              f"giving you some EXP.\n"
              f"\n"
              f"Gold can be used at shops, either to buy items or upgrade.\n"
              f"\n"
              f"EXP, when accumulated enough, allows you to LEVEL UP, boosting your base attributes.\n")

    print(f"\n\n")

    display.current_map(character, current_board)

    print(f"\n"
          f"Now that you have the key to the exit, you are now able to embark on \n"
          f"your quest to {Fore.LIGHTYELLOW_EX}take back the throne{Fore.RESET}.\n"
          f"\n"
          f"You're journey is now yours and yours alone.\n"
          f"\n"
          f"Venture, hunt, loot, and spend. Do anything and everything you can to \n"
          f"strengthen yourself enough to one day kill {Fore.RED}{bbeg["name"].upper()}{Fore.RESET}.\n")
    input(f"{Fore.WHITE}{Style.BRIGHT}Press Enter to {Fore.RESET}EXIT THE DUNGEONS: {Style.RESET_ALL}")

    print(f"\n\n\n"
          f"{Style.BRIGHT}Good luck.{Style.RESET_ALL}"
          f"\n\n\n")
    input(f"{Fore.WHITE}{Style.BRIGHT}Press Enter to continue: {Style.RESET_ALL}")

    check.move_character("s", character)


def run_battle(character, enemy, round_count=1):
    """
    Drive the battle.
    """
    player_alive = True
    enemy_alive = True

    player_round_counter = round_count
    enemy_round_counter = round_count

    enemy_action_list = enemy["actions"]

    character["reduce_damage"] = math.ceil(character["DEF"] // 4)
    enemy["reduce_damage"] = math.ceil(character["DEF"] // 4)

    while player_alive and enemy_alive:
        for enemy_action in enemy_action_list:
            display.battle_status(character, enemy, player_round_counter)

            if character["AGI"] >= enemy["AGI"]:
                player_battle_flow(character, enemy, player_round_counter)
                player_alive = check.if_alive(character)
                if not player_alive:
                    break
                battle.skill_effect_time(character, player_round_counter)
                player_round_counter += 1

                enemy_battle_flow(character, enemy, enemy_action, enemy_round_counter)
                enemy_alive = check.if_alive(enemy)
                if not enemy_alive:
                    break
                battle.skill_effect_time(enemy, player_round_counter)
                enemy_round_counter += 1

            elif character["AGI"] < enemy["AGI"]:
                enemy_battle_flow(character, enemy, enemy_action, enemy_round_counter)
                enemy_alive = check.if_alive(enemy)
                if not enemy_alive:
                    break
                battle.skill_effect_time(enemy, player_round_counter)
                enemy_round_counter += 1

                player_battle_flow(character, enemy, player_round_counter)
                player_alive = check.if_alive(character)
                if not player_alive:
                    break
                battle.skill_effect_time(character, player_round_counter)
                player_round_counter += 1

    if not enemy_alive:
        character["EXP"] -= enemy["EXP"]
        character["gold"] += enemy["gold"]
        print(f"\n\n\n"
              f"{Style.BRIGHT}You won!{Style.RESET_ALL}\n"
              f"\n"
              f"Gained {enemy["EXP"]} EXP and {enemy["gold"]} gold!\n")
        check.level_up(character)

    character["buff"] = {"ATK": {"effect": 0, "time": 0},
                         "DEF": {"effect": 0, "time": 0},
                         "AGI": {"effect": 0, "time": 0},
                         "LUK": {"effect": 0, "time": 0}}

    character["debuff"] = {"ATK": {"effect": 0, "time": 0},
                           "DEF": {"effect": 0, "time": 0},
                           "AGI": {"effect": 0, "time": 0},
                           "LUK": {"effect": 0, "time": 0}}

    character["continuous_damage"] = {"effect": 0, "time": 0}


def player_battle_flow(character, enemy, round_count):
    """
    Drive player battle flow.
    """
    player_action_list = ["attack", "defend", "skill", "item"]

    player_skill_list = get.class_list(character["skill_class"])["skill_list"]
    player_item_list = character["inventory"].keys()

    action_made = False
    while not action_made:
        player_action = battle.ask_player_input(player_action_list)
        if player_action == "attack":
            battle.attack(character, enemy)
            action_made = True
        elif player_action == "defend":
            battle.defend(character)
            action_made = True
        elif player_action == "skill":
            sp_discount = 0
            if character["species"] == "elf":
                sp_discount = 1

            chosen_skill = ""
            while chosen_skill != "back":
                chosen_skill = battle.ask_player_input(player_skill_list)
                if chosen_skill != "back":
                    usable_skill = battle.skill_usable(chosen_skill, character, sp_discount)
                    if usable_skill:
                        battle.use_skill(chosen_skill, round_count, character, enemy, sp_discount)
                        action_made = True
                        break
                    else:
                        print(f"\n\n\n{Style.BRIGHT}Not enough SP!{Style.RESET_ALL}\n\n\n")

        elif player_action == "item":
            display.inventory(character)
            if not player_item_list:
                print(f"\n\n\n{Style.BRIGHT}No items to chose from.{Style.RESET_ALL}\n\n\n")
            else:
                chosen_item = ""
                while chosen_item != "back":
                    effect_bonus = 0
                    if character["species"] == "human":
                        effect_bonus = 2
                    chosen_item = battle.ask_player_input(player_item_list)
                    if chosen_item != "back":
                        battle.use_item(chosen_item, character, effect_bonus)
                        action_made = True
                        break

    character["current_HP"] -= character["continuous_damage"]["effect"]


def enemy_battle_flow(character, enemy, enemy_action, round_count):
    """
    Drive enemy battle flow.
    """
    if enemy_action == "attack":
        battle.attack(enemy, character)
    elif enemy_action == "defend":
        battle.defend(enemy)
    elif enemy_action == "skill":
        chosen_skill = enemy["skill"]
        battle.use_skill(chosen_skill, round_count, enemy, character)
    enemy["current_HP"] -= enemy["continuous_damage"]["effect"]


def game():
    """
    Drive the game.
    """
    print("==============================\n"
          "\n\n"
          f"\t {Style.BRIGHT}+++ BIRTH RIGHT +++{Style.RESET_ALL}\n"
          "\n"
          f"   {Fore.GREEN}Game By: Kanon Nishiyama{Fore.RESET}\n"
          "\n\n"
          "==============================\n")
    input(f"{Fore.WHITE}{Style.BRIGHT}Press Enter to {Fore.RESET}START{Style.RESET_ALL}: ")

    print("\n\n\n"
          "\n\n\n"
          "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
          "\n"
          f"Welcome to {Style.BRIGHT}{Fore.BLUE}BIRTH RIGHT{Style.RESET_ALL}.\n"
          f"\n"
          f"A simple RPG where you play as the {Fore.LIGHTYELLOW_EX}Heir to the Throne{Fore.RESET}, currently \n"
          f"captured and imprisoned by the {Fore.RED}King's Advisor{Fore.RESET} who had commited \n"
          f"regicide and stolen the throne.\n"
          f"\n"
          f"You, perhaps driven by justice or revenge, must break out of your \n"
          f"confines and train to strengthen yourself enough to one day defeat \n"
          f"this evil tyrant and take back what is rightfully yours...\n"
          "\n"
          "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    input(f"{Fore.WHITE}{Style.BRIGHT}Press Enter to continue to {Fore.RESET}CHARACTER CREATION{Style.RESET_ALL}: ")

    player_character = get.blank_character()
    bbeg = get.unnamed_bbeg()
    
    print("\n\n\n")
    create_new_character(player_character, bbeg)

    print("\n\n\n")
    tutorial(player_character, bbeg)

    current_board = get.main_board()
    player_alive = True
    bbeg_alive = True
    clear_main = False

    while not clear_main and player_alive:
        display.current_map(player_character, current_board)

        player_input = input(f"{Fore.WHITE}{Style.BRIGHT}Player command: {Style.RESET_ALL}")
        check.validate_exploration_command(player_input, player_character, current_board)

        encounter = check.enemy_encounter(player_character, current_board)

        if encounter:
            enemy = get.random_enemy(player_character, current_board)
            run_battle(player_character, enemy)
            player_alive = check.if_alive(player_character)

        current_coordinate = (player_character["x-coordinate"], player_character["x-coordinate"])

        try:
            if current_board[current_coordinate]["symbol"] == "exit" and player_character["LVL"] == 3:
                print(f"\n\n\n"
                      f"You are now strong enough to challenge {bbeg["name"].upper()} for the throne.\n"
                      f"\n"
                      f"If you enter the castle, there is no going back.\n"
                      f"This will be the end.\n")
                confirm = input("Do you want to enter your FINAL BATTLE? (y/n): ").strip().lower()
                if confirm == "y":
                    clear_main = True
                elif confirm == "n":
                    clear_main = False
                else:
                    print(f"\n\n\n{Style.BRIGHT}Please confirm your choice.{Style.RESET_ALL}\n\n\n")
        except KeyError:
            pass

    if player_alive and clear_main:
        run_battle(player_character, bbeg)
        bbeg_alive = check.if_alive(bbeg)

    if not bbeg_alive and player_alive:
        print(f"\n\n\n"
              f"{Style.BRIGHT}CONGRATULATIONS!!!{Style.RESET_ALL}\n"
              f"\n"
              f"You have done it. You have killed {Fore.RED}{bbeg["name"].upper()}{Fore.RESET} "
              f"and taken back what \n"
              f"was rightfully yours.\n"
              f"\n"
              f"With you back on the throne of {player_character["kingdom"].upper()}, the kingdom "
              f"will once again \n"
              f"flourish and thrive under your rule...\n"
              f"\n"
              f"But that is a story for another time.\n"
              f"For now, let us celebrate for your victory as you rightfully claim your...\n")
        input(f"{Fore.WHITE}{Style.BRIGHT}Press Enter to {Fore.RESET}END GAME{Style.RESET_ALL}: ")

        print(f"\n\n\n"
              f"==============================\n"
              f"\n\n"
              f"\t {Style.BRIGHT}+++ BIRTH RIGHT +++{Style.RESET_ALL}\n"
              f"   {Style.BRIGHT}THANK YOU FOR PLAYING!!!{Style.RESET_ALL}\n"
              f"\n"
              f"   {Fore.GREEN}Game By: Kanon Nishiyama{Fore.RESET}\n"
              f"\n\n"
              f"==============================\n")

    if not player_alive:
        print(f"\n\n\n"
              f"Y{Style.BRIGHT}You Died.{Style.RESET_ALL}\n"
              f"\n"
              f"As the light begins to fade, you lament the future for your kingdom as it's \n"
              f"one and only heir takes their last breath.\n"
              f"\n"
              f"If only you could have done something...\n")
        confirm = input("Do you want to try again? (y/n): ").strip().lower()
        if confirm == "y":
            game()
        elif confirm == "n":
            pass
        else:
            print(f"\n\n\n{Style.BRIGHT}Please confirm your choice.{Style.RESET_ALL}\n\n\n")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
