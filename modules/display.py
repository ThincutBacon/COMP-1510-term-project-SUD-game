"""

Kanon Nishiyama
A1415217

"""
from modules import get


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

    skill_list = get.class_list(character['skill_class'])['skill_list']
    first_skill = f"{format(skill_list[0].title(), '15')}: 2323 SP "
    second_skill = f"{format(skill_list[1].title(), '15')}: 2323 SP "
    third_skill = f"{format(skill_list[2].title(), '15')}: 2323 SP "

    hp = f"HP: {format(character['current_HP'], '3')} / {format(character['max_HP'], '3')}"
    sp = f"SP: {format(character['current_SP'], '3')} / {format(character['max_SP'], '3')}"

    atk_attribute = f"ATK: {format(character['ATK'], '3')}"
    def_attribute = f"DEF: {format(character['DEF'], '3')}"
    agi_attribute = f"AGI: {format(character['AGI'], '3')}"
    luk_attribute = f"LUK: {format(character['LUK'], '3')}"

    print(f"==============================================\n"
          f"| {format(character_name, '42')} |\n"
          f"| {format(class_and_species, '42')} |\n"
          f"| {format(kingdom_name, '42')} |\n"
          f"|--------------------------------------------|\n"
          f"| {format("STATS", '20')}| {format("ATTRIBUTES", '20')} |\n"
          f"| {format("=============", '20')}| {format("=============", '20')} |\n"
          f"| {format(hp, '20')}| {format(atk_attribute, '20')} |\n"
          f"| {format(sp, '20')}| {format(def_attribute, '20')} |\n"
          f"| {format("", '20')}| {format(agi_attribute, '20')} |\n"
          f"| {format("", '20')}| {format(luk_attribute, '20')} |\n"
          f"|--------------------------------------------|\n"
          f"| {format("SKILLS", '42')} |\n"
          f"| {format("=============", '42')} |\n"
          f"| {format(first_skill, '42')} |\n"
          f"| {format(second_skill, '42')} |\n"
          f"| {format(third_skill, '42')} |\n"
          f"==============================================\n")


def main():
    """
    Drive the program.
    """
    character = get.blank_character()
    character["name"] = "Tohru"
    character["kingdom"] = "Heilia"
    character["species_adjective"] = "elven"
    character["skill_class"] = "mage"
    character_info(character)


if __name__ == "__main__":
    main()
