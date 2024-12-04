"""

Kanon Nishiyama
A1415217

"""


from colorama import Style, Fore

from modules import create_character, get, display, check


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


def tutorial(character):
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
          f"I would recommend looking whenever you move to a new location, as \n"
          f"it can provide you with hints on what to do or where to go.\n")
    input(f"{Fore.WHITE}{Style.BRIGHT}Press Enter to continue: {Style.RESET_ALL}")


def game():
    """
    Drive the game.
    """
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

    """

    player_character = get.blank_character()
    bbeg = get.unnamed_bbeg()

    """
    
    print("\n\n\n")
    create_new_character(player_character, bbeg)
    
    """

    print("\n\n\n")
    tutorial(player_character)

    current_board = get.main_board()
    clear_main = False
    while not clear_main:
        display.current_map(player_character, current_board)
        break


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
