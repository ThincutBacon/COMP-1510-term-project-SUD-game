"""

Kanon Nishiyama
A1415217

"""


def character_info(character):
    """
    Print character information.

    :param character: a dictionary
    :precondition: character must be a dictionary from get.blank_character function
    :postcondition: print character information for the player to easily read

    >>> character_info()
    ''
    """
    print(
        ""
    )


def main():
    """
    Drive the program.
    """

    hp = f"HP: {format(3, '3')} / {format(51, '3')}"
    sp = f"SP: {format(4, '3')} / {format(10, '3')}"
    str = f"STR: {format(4, '3')}"
    defn = f"DEF: {format(4, '3')}"
    print("==================\n| TOHRU\n| Heir to the throne\n| \n"
          f"| {format("STATS", '15')} |  {format("ATTRIBUTES", '15')}\n"
          f"| {format("============", '15')} |  {format("============", '15')}\n"
          f"| {format(hp, '15')} |  {format(str, '15')}\n"
          f"| {format(sp, '15')} |  {format(defn, '15')}\n")


if __name__ == "__main__":
    main()
