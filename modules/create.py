"""

Kanon Nishiyama
A1415217

"""
from pprint import pprint


def tutorial_board():
    """
    Return the tutorial board.

    :return: a dictionary containing tuples containing coordinates as keys which are paired with a dictionary
             containing the coordinates information

    >>> tutorial_board() #doctest: +ELLIPSIS
    {(0, 0): {'name': 'The Dungeons - Hallway', 'look': 'There is no light inside the dark ...
    """
    return {(0, 0): {"name": "The Dungeons - Hallway",
                     "look": "There is no light inside the dark cavernous halls of the dungeons, "
                             "the only sliver of light pours in from the slits of the door which withholds "
                             "your freedom.\n"
                             "You see a glint of something in the corner of your eye.\n"
                             "Maybe you could SCAVENGE to see what it is.",
                     "area": "safe",
                     "scavenge": "key",
                     "action": "none",
                     "walls": ["n", "s", "w"]},
            (0, 1): {"name": "The Dungeons - The Exit",
                     "look": "Your only exit lies in front of you, locked and guarded from outside.\n"
                             "Once you EXIT, you are sure to enter battle with the guards.",
                     "area": "safe",
                     "scavenge": "none",
                     "action": "exit",
                     "walls": ["n", "s", "e"]}}


def main_board():
    """
    Return the main board.

    :return: a dictionary containing tuples containing coordinates as keys which are paired with a dictionary
             containing the coordinates information

    >>> main_board() #doctest: +ELLIPSIS
    {(0, 0): {'name': 'The Dungeons - Hallway', 'look': 'What is left of the dungeons is a shell ...
    """
    return {(0, 0): {"name": "The Dungeons - Hallway",
                     "look": "What is left of the dungeons is a shell of what used to confine you. "
                             "Only rats roam these halls now.",
                     "area": "dungeon",
                     "scavenge": "none",
                     "action": "none",
                     "walls": ["n", "s", "w"]},
            (0, 1): {"name": "The Dungeons - The Exit",
                     "look": "The slain bodies of the guards remain discarded next to the door.",
                     "area": "safe",
                     "scavenge": "none",
                     "action": "none",
                     "walls": ["n", "e"]},
            (0, 2): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (0, 3): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (0, 4): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},

            (1, 0): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (1, 1): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (1, 2): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (1, 3): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (1, 4): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},

            (2, 0): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (2, 1): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (2, 2): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (2, 3): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (2, 4): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},

            (3, 0): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (3, 1): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (3, 2): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (3, 3): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (3, 4): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},

            (4, 0): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (4, 1): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (4, 2): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (4, 3): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []},
            (4, 4): {"name": "",
                     "look": "",
                     "area": "",
                     "scavenge": "",
                     "action": "",
                     "walls": []}}


def main():
    """
    Drive the program.
    """
    test = tutorial_board()
    print(test[(0, 0)]["name"])
    print(test[(0, 0)]["look"])
    print(test[(0, 0)]["area"])


if __name__ == "__main__":
    main()
