from unittest import TestCase

from colorama import Style

from modules.get import class_list


class TestGetClassList(TestCase):

    def test_get_class_list_contains_list_all_key(self):
        result = class_list()
        self.assertIn("list_all", result)

    def test_get_class_list_list_all_value_is_a_string(self):
        result = class_list()
        actual = result["list_all"]
        expected = ("==========\n" +
                    Style.BRIGHT + "WARRIOR\n" + Style.RESET_ALL +
                    "\"For those who fight with endurance.\"\n"
                    "\n" +
                    Style.BRIGHT + "SCOUT\n" + Style.RESET_ALL +
                    "\"For those who fight with deadly accuracy.\"\n"
                    "\n" +
                    Style.BRIGHT + "MAGE\n" + Style.RESET_ALL +
                    "\"For those who fight by leveling the playing field.\"\n"
                    "==========\n")

        self.assertEqual(expected, actual)

    def test_get_class_list_contains_warrior_key(self):
        result = class_list()
        self.assertIn("warrior", result)

    def test_get_class_list_contains_elf_key(self):
        result = class_list()
        self.assertIn("scout", result)

    def test_get_class_list_contains_mage_key(self):
        result = class_list()
        self.assertIn("mage", result)

    def test_get_class_list_warrior_contains_class_key(self):
        result = class_list("warrior")
        self.assertIn("class", result)

    def test_get_class_list_warrior_class_value_is_warrior(self):
        result = class_list("warrior")
        actual = result["class"]
        expected = "warrior"
        self.assertEqual(expected, actual)

    def test_get_class_list_warrior_contains_desc_key(self):
        result = class_list("warrior")
        self.assertIn("desc", result)

    def test_get_class_list_warrior_desc_value_is_a_string(self):
        result = class_list("warrior")
        actual = result["desc"]
        expected = ("Warrior's fight slow battles with a shield in hand, toughing it \n"
                    "out until their enemies fall in battle.\n"
                    "\n"
                    f"{Style.BRIGHT}Class Skills:{Style.RESET_ALL}\n"
                    f"{Style.BRIGHT}Shield{Style.RESET_ALL} - Increases your DEF\n"
                    f"{Style.BRIGHT}Shield Bash{Style.RESET_ALL} - Attacks while raising "
                    f"your DEF\n"
                    f"{Style.BRIGHT}Battle Cry{Style.RESET_ALL} - Weakens enemy DEF\n")

        self.assertEqual(expected, actual)

    def test_get_class_list_warrior_contains_skill_list_key(self):
        result = class_list("warrior")
        self.assertIn("skill_list", result)

    def test_get_class_list_warrior_skill_list_value_is_list(self):
        result = class_list("warrior")
        actual = result["skill_list"]
        expected = ["shield", "shield bash", "battle cry"]
        self.assertEqual(expected, actual)

    def test_get_class_list_elf_contains_class_key(self):
        result = class_list("scout")
        self.assertIn("class", result)

    def test_get_class_list_elf_class_value_is_elf(self):
        result = class_list("scout")
        actual = result["class"]
        expected = "scout"
        self.assertEqual(expected, actual)

    def test_get_class_list_elf_contains_desc_key(self):
        result = class_list("scout")
        self.assertIn("desc", result)

    def test_get_class_list_elf_desc_value_is_a_string(self):
        result = class_list("scout")
        actual = result["desc"]
        expected = ("Scout's fight quick battles, inflicting fatal damage before their \n"
                    "enemies have a chance to hurt them back.\n"
                    "\n"
                    f"{Style.BRIGHT}Class Skills:{Style.RESET_ALL}\n"
                    f"{Style.BRIGHT}Sharper Edge{Style.RESET_ALL} - Increases your ATK\n"
                    f"{Style.BRIGHT}Focus Attack{Style.RESET_ALL} - Attacks while increasing "
                    f"your LUK\n"
                    f"{Style.BRIGHT}Haste{Style.RESET_ALL} - Increases your AGI\n")

        self.assertEqual(expected, actual)

    def test_get_class_list_scout_contains_skill_list_key(self):
        result = class_list("scout")
        self.assertIn("skill_list", result)

    def test_get_class_list_scout_skill_list_value_is_list(self):
        result = class_list("scout")
        actual = result["skill_list"]
        expected = ["sharper edge", "focus attack", "haste"]
        self.assertEqual(expected, actual)

    def test_get_class_list_mage_contains_class_key(self):
        result = class_list("mage")
        self.assertIn("class", result)

    def test_get_class_list_mage_class_value_is_mage(self):
        result = class_list("mage")
        actual = result["class"]
        expected = "mage"
        self.assertEqual(expected, actual)

    def test_get_class_list_mage_contains_desc_key(self):
        result = class_list("mage")
        self.assertIn("desc", result)

    def test_get_class_list_mage_desc_value_is_a_string(self):
        result = class_list("mage")
        actual = result["desc"]
        expected = ("Mage's fight a careful battle, slowly chipping away at their enemies \n"
                    "health while maintaining their own.\n"
                    "\n"
                    f"{Style.BRIGHT}Class Skills:{Style.RESET_ALL}\n"
                    f"{Style.BRIGHT}Fireball{Style.RESET_ALL} - Continuously burns the enemy\n"
                    f"{Style.BRIGHT}Freezing Touch{Style.RESET_ALL} - Slows an enemy's AGI\n"
                    f"{Style.BRIGHT}Healing Light{Style.RESET_ALL} - Heals your HP\n")

        self.assertEqual(expected, actual)

    def test_get_class_list_mage_contains_skill_list_key(self):
        result = class_list("mage")
        self.assertIn("skill_list", result)

    def test_get_class_list_mage_skill_list_value_is_list(self):
        result = class_list("mage")
        actual = result["skill_list"]
        expected = ["fireball", "freezing touch", "healing light"]
        self.assertEqual(expected, actual)
