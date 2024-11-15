"""

Kanon Nishiyama
A1415217

"""


def species_list(select=None):
    """
    Returns species information.

    :param select: a string
    :precondition: select must equal None or one of the keys within entire_species_list
    :return: if select equals None, returns the entire dictionary
    :return: if select equals a key, returns a single species dictionary

    >>> species_list()
    ''
    """
    entire_species_list = {"list_all": "==========\n"
                                       "HUMAN\n"
                                       "\"The most versatile of species.\"\n"
                                       "\n"
                                       "ELF\n"
                                       "\"The graceful guardians of the forests.\"\n"
                                       "\n"
                                       "DWARF\n"
                                       "\"Inhabitants of the deepest caves and the highest mountains.\"\n"
                                       "==========\n",
                           "human": {"name": "human",
                                     "desc": "Although average in most aspects, they possess strong survival "
                                             "prowess and the ability to utilize items to their fullest potential.\n"
                                             "\n"
                                             "Highest Attributes: ATK and LUK\n"
                                             "Species Bonus: All items gain an additional +2 to their effects\n",
                                     "HP": 0,
                                     "SP": 0,
                                     "ATK": 0,
                                     "DEF": 0,
                                     "AGI": 0,
                                     "LUK": 0},
                           "elf": {"name": "elf",
                                   "desc": "With their long life spans and equally cumulative knowledge, they are "
                                           "known to be the best when it comes to efficiently using skills and "
                                           "spells.\n"
                                           "\n"
                                           "Highest Attributes: SP and AGI\n"
                                           "Species Bonus: All skills cost -1 SP\n",
                                   "HP": 0,
                                   "SP": 0,
                                   "ATK": 0,
                                   "DEF": 0,
                                   "AGI": 0,
                                   "LUK": 0},
                           "dwarf": {"name": "dwarf",
                                     "desc": "To withstand the frigid cold of the mountain tops and the sweltering "
                                             "heat of a forge, they have developed a thicker skin then many.\n"
                                             "\n"
                                             "Highest Attributes: HP and DEF\n"
                                             "Species Bonus: All equipment gain an additional +1 to their effects\n",
                                     "HP": 0,
                                     "SP": 0,
                                     "ATK": 0,
                                     "DEF": 0,
                                     "AGI": 0,
                                     "LUK": 0}}

    if select:
        return entire_species_list[select]
    else:
        return entire_species_list


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
