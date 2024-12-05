from unittest import TestCase

from colorama import Style

from modules.get import species_list


class TestGetSpeciesList(TestCase):

    def test_get_species_list_contains_list_all_key(self):
        result = species_list()
        self.assertIn("list_all", result)

    def test_get_species_list_contains_human_key(self):
        result = species_list()
        self.assertIn("human", result)

    def test_get_species_list_contains_elf_key(self):
        result = species_list()
        self.assertIn("elf", result)

    def test_get_species_list_contains_dwarf_key(self):
        result = species_list()
        self.assertIn("dwarf", result)

    def test_get_species_list_human_contains_name_key(self):
        result = species_list("human")
        self.assertIn("name", result)

    def test_get_species_list_human_name_value_is_human(self):
        result = species_list("human")
        actual = result["name"]
        expected = "human"
        self.assertEqual(expected, actual)

    def test_get_species_list_human_contains_adjective_key(self):
        result = species_list("human")
        self.assertIn("adjective", result)

    def test_get_species_list_human_adjective_value_is_human(self):
        result = species_list("human")
        actual = result["adjective"]
        expected = "human"
        self.assertEqual(expected, actual)

    def test_get_species_list_human_contains_desc_key(self):
        result = species_list("human")
        self.assertIn("desc", result)

    def test_get_species_list_human_adjective_value_is_a_string(self):
        result = species_list("human")
        actual = result["desc"]
        expected = ("Although average in most aspects, they possess strong survival \n"
                    "prowess and the ability to utilize items to their fullest potential.\n"
                    "\n"
                    f"{Style.BRIGHT}Highest Attributes:{Style.RESET_ALL} ATK and LUK\n"
                    f"{Style.BRIGHT}Species Bonus:{Style.RESET_ALL} All items gain an "
                    f"additional +2 to their effects\n")

        self.assertEqual(expected, actual)

    def test_get_species_list_human_contains_HP_key(self):
        result = species_list("human")
        self.assertIn("HP", result)

    def test_get_species_list_human_HP_value_is_15(self):
        result = species_list("human")
        actual = result["HP"]
        expected = 15
        self.assertEqual(expected, actual)

    def test_get_species_list_human_contains_SP_key(self):
        result = species_list("human")
        self.assertIn("SP", result)

    def test_get_species_list_human_SP_value_is_10(self):
        result = species_list("human")
        actual = result["SP"]
        expected = 10
        self.assertEqual(expected, actual)

    def test_get_species_list_human_contains_ATK_key(self):
        result = species_list("human")
        self.assertIn("ATK", result)

    def test_get_species_list_human_ATK_value_is_15(self):
        result = species_list("human")
        actual = result["ATK"]
        expected = 15
        self.assertEqual(expected, actual)

    def test_get_species_list_human_contains_DEF_key(self):
        result = species_list("human")
        self.assertIn("DEF", result)

    def test_get_species_list_human_DEF_value_is_5(self):
        result = species_list("human")
        actual = result["DEF"]
        expected = 5
        self.assertEqual(expected, actual)

    def test_get_species_list_human_contains_AGI_key(self):
        result = species_list("human")
        self.assertIn("AGI", result)

    def test_get_species_list_human_AGI_value_is_5(self):
        result = species_list("human")
        actual = result["AGI"]
        expected = 5
        self.assertEqual(expected, actual)

    def test_get_species_list_human_contains_LUK_key(self):
        result = species_list("human")
        self.assertIn("LUK", result)

    def test_get_species_list_human_LUK_value_is_10(self):
        result = species_list("human")
        actual = result["LUK"]
        expected = 10
        self.assertEqual(expected, actual)

    def test_get_species_list_elf_contains_name_key(self):
        result = species_list("elf")
        self.assertIn("name", result)

    def test_get_species_list_elf_name_value_is_elf(self):
        result = species_list("elf")
        actual = result["name"]
        expected = "elf"
        self.assertEqual(expected, actual)

    def test_get_species_list_elf_contains_adjective_key(self):
        result = species_list("elf")
        self.assertIn("adjective", result)

    def test_get_species_list_elf_adjective_value_is_elven(self):
        result = species_list("elf")
        actual = result["adjective"]
        expected = "elven"
        self.assertEqual(expected, actual)

    def test_get_species_list_elf_contains_desc_key(self):
        result = species_list("elf")
        self.assertIn("desc", result)

    def test_get_species_list_elf_adjective_value_is_a_string(self):
        result = species_list("elf")
        actual = result["desc"]
        expected = ("With their long life spans and equally cumulative knowledge, they are \n"
                    "known to be the best when it comes to efficiently using skills and \n"
                    "spells.\n"
                    "\n"
                    f"{Style.BRIGHT}Highest Attributes:{Style.RESET_ALL} SP and AGI\n"
                    f"{Style.BRIGHT}Species Bonus:{Style.RESET_ALL} All skills cost -1 SP\n")

        self.assertEqual(expected, actual)

    def test_get_species_list_elf_contains_HP_key(self):
        result = species_list("elf")
        self.assertIn("HP", result)

    def test_get_species_list_elf_HP_value_is_15(self):
        result = species_list("elf")
        actual = result["HP"]
        expected = 15
        self.assertEqual(expected, actual)

    def test_get_species_list_elf_contains_SP_key(self):
        result = species_list("elf")
        self.assertIn("SP", result)

    def test_get_species_list_elf_SP_value_is_15(self):
        result = species_list("elf")
        actual = result["SP"]
        expected = 15
        self.assertEqual(expected, actual)

    def test_get_species_list_elf_contains_ATK_key(self):
        result = species_list("elf")
        self.assertIn("ATK", result)

    def test_get_species_list_elf_ATK_value_is_10(self):
        result = species_list("elf")
        actual = result["ATK"]
        expected = 10
        self.assertEqual(expected, actual)

    def test_get_species_list_elf_contains_DEF_key(self):
        result = species_list("elf")
        self.assertIn("DEF", result)

    def test_get_species_list_elf_DEF_value_is_5(self):
        result = species_list("elf")
        actual = result["DEF"]
        expected = 5
        self.assertEqual(expected, actual)

    def test_get_species_list_elf_contains_AGI_key(self):
        result = species_list("elf")
        self.assertIn("AGI", result)

    def test_get_species_list_elf_AGI_value_is_15(self):
        result = species_list("elf")
        actual = result["AGI"]
        expected = 15
        self.assertEqual(expected, actual)

    def test_get_species_list_elf_contains_LUK_key(self):
        result = species_list("elf")
        self.assertIn("LUK", result)

    def test_get_species_list_elf_LUK_value_is_5(self):
        result = species_list("elf")
        actual = result["LUK"]
        expected = 5
        self.assertEqual(expected, actual)

    def test_get_species_list_dwarf_contains_name_key(self):
        result = species_list("dwarf")
        self.assertIn("name", result)

    def test_get_species_list_dwarf_name_value_is_dwarf(self):
        result = species_list("dwarf")
        actual = result["name"]
        expected = "dwarf"
        self.assertEqual(expected, actual)

    def test_get_species_list_dwarf_contains_adjective_key(self):
        result = species_list("dwarf")
        self.assertIn("adjective", result)

    def test_get_species_list_dwarf_adjective_value_is_dwarven(self):
        result = species_list("dwarf")
        actual = result["adjective"]
        expected = "dwarven"
        self.assertEqual(expected, actual)

    def test_get_species_list_dwarf_contains_desc_key(self):
        result = species_list("dwarf")
        self.assertIn("desc", result)

    def test_get_species_list_dwarf_adjective_value_is_a_string(self):
        result = species_list("dwarf")
        actual = result["desc"]
        expected = ("To withstand the frigid cold of the mountain tops and the sweltering \n"
                    "heat of a forge, they have developed a thicker skin then many.\n"
                    "\n"
                    f"{Style.BRIGHT}Highest Attributes:{Style.RESET_ALL} HP and DEF\n"
                    f"{Style.BRIGHT}Species Bonus:{Style.RESET_ALL} All equipment gain "
                    f"an additional +1 to their effects\n")

        self.assertEqual(expected, actual)

    def test_get_species_list_dwarf_contains_HP_key(self):
        result = species_list("dwarf")
        self.assertIn("HP", result)

    def test_get_species_list_dwarf_HP_value_is_25(self):
        result = species_list("dwarf")
        actual = result["HP"]
        expected = 25
        self.assertEqual(expected, actual)

    def test_get_species_list_dwarf_contains_SP_key(self):
        result = species_list("dwarf")
        self.assertIn("SP", result)

    def test_get_species_list_dwarf_SP_value_is_5(self):
        result = species_list("dwarf")
        actual = result["SP"]
        expected = 5
        self.assertEqual(expected, actual)

    def test_get_species_list_dwarf_contains_ATK_key(self):
        result = species_list("dwarf")
        self.assertIn("ATK", result)

    def test_get_species_list_dwarf_ATK_value_is_10(self):
        result = species_list("dwarf")
        actual = result["ATK"]
        expected = 10
        self.assertEqual(expected, actual)

    def test_get_species_list_dwarf_contains_DEF_key(self):
        result = species_list("dwarf")
        self.assertIn("DEF", result)

    def test_get_species_list_dwarf_DEF_value_is_15(self):
        result = species_list("dwarf")
        actual = result["DEF"]
        expected = 15
        self.assertEqual(expected, actual)

    def test_get_species_list_dwarf_contains_AGI_key(self):
        result = species_list("dwarf")
        self.assertIn("AGI", result)

    def test_get_species_list_dwarf_AGI_value_is_5(self):
        result = species_list("dwarf")
        actual = result["AGI"]
        expected = 5
        self.assertEqual(expected, actual)

    def test_get_species_list_dwarf_contains_LUK_key(self):
        result = species_list("dwarf")
        self.assertIn("LUK", result)

    def test_get_species_list_dwarf_LUK_value_is_10(self):
        result = species_list("dwarf")
        actual = result["LUK"]
        expected = 10
        self.assertEqual(expected, actual)
