"""

Kanon Nishiyama
A1415217

"""


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

    >>> function()
    ''
    """
    pass


def defend(defender):
    """
    Sentence.

    :param x: x
    :precondition: x
    :postcondition: x
    :return: x

    >>> function()
    ''
    """
    pass


def use_skill(skill, user, receiver):
    """
    Sentence.

    :param x: x
    :precondition: x
    :postcondition: x
    :return: x

    >>> function()
    ''
    """
    pass


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
    pass


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
