"""

Kanon Nishiyama
A1415217

"""


def tutorial_board():
    """
    Return the tutorial board.

    :return: a dictionary containing tuples containing coordinates as keys which are paired with a dictionary
             containing the coordinates information

    >>> tutorial_board() #doctest: +ELLIPSIS
    {(0, 0): {'name': 'The Dungeons - Hallway', 'look': 'There is no light inside the dark ...
    """
    return {
            (0, 0): {"name": "The Dungeons - Hallway",
                     "look": "There is no light inside the dark cavernous halls of the dungeons, "
                             "the only sliver of light pours in from the slits of the door which withholds "
                             "your freedom. You see a glint of something in the corner of your eye. Maybe "
                             "you could SCAVENGE to see what it is.",
                     "area": "safe",
                     "scavenge": "none",
                     "action": "none",
                     "walls": ["n", "s", "w"]},
            (0, 1): {"name": "The Dungeons - The Exit",
                     "look": "The key to your freedom lies in front of you, locked and guarded from outside. "
                             "Once you EXIT, you are sure to enter battle with the guards outside.",
                     "area": "safe",
                     "scavenge": "none",
                     "action": "exit",
                     "walls": ["n", "s", "e"]}
            }


def main_board():
    """
    Return the main board.

    :return: a dictionary containing tuples containing coordinates as keys which are paired with a dictionary
             containing the coordinates information

    >>> main_board() #doctest: +ELLIPSIS
    {(0, 0): {'name': 'The Dungeons - Hallway', 'look': 'There is no light inside the dark ...
    """
    return {(0, 0): {}, (0, 1): {}, (0, 2): {}, (0, 3): {}, (0, 4): {},
            (1, 0): {}, (1, 1): {}, (1, 2): {}, (1, 3): {}, (1, 4): {},
            (2, 0): {}, (2, 1): {}, (2, 2): {}, (2, 3): {}, (2, 4): {},
            (3, 0): {}, (3, 1): {}, (3, 2): {}, (3, 3): {}, (3, 4): {},
            (4, 0): {}, (4, 1): {}, (4, 2): {}, (4, 3): {}, (4, 4): {}}


def main():
    """
    Drive the program.
    """
    test = tutorial_board()
    print(test[(0, 0)]["look"])


if __name__ == "__main__":
    main()
