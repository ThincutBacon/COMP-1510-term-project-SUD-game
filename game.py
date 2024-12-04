"""

Kanon Nishiyama
A1415217

"""


from colorama import Style, Fore

from modules import create_character, get, display


def create_new_character(character, bbeg):
    """
    Drive the character creation.
    """
    confirm_create = False
    while not confirm_create:
        print("\n\n"
              f"{Style.BRIGHT}===== CREATE CHARACTER ====={Style.RESET_ALL}\n")
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
    input(f"Press Enter to {Style.BRIGHT}START{Style.RESET_ALL}: ")

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
    input(f"Press Enter to continue to {Style.BRIGHT}CHARACTER CREATION{Style.RESET_ALL}: ")

    player_character = get.blank_character()
    bbeg = get.unnamed_bbeg()

    print("\n\n\n")
    create_new_character(player_character, bbeg)

    print("\n\n"
          f"{Style.BRIGHT}===== TUTORIAL ====={Style.RESET_ALL}\n"
          "\n")

    current_board = get.tutorial_board()
    clear_tutorial = False
    while not clear_tutorial:
        display.current_map(player_character, current_board)
        break

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
