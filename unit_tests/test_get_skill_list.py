from unittest import TestCase

from modules.get import skill_list


class TestGetSkillList(TestCase):

    def test_get_skill_list_contains_shield_key(self):
        result = skill_list()
        self.assertIn("shield", result)

    def test_get_skill_list_shield_contains_name_key(self):
        result = skill_list("shield")
        self.assertIn("name", result)

    def test_get_skill_list_shield_name_value_is_shield(self):
        result = skill_list("shield")
        actual = result["name"]
        expected = "shield"
        self.assertEqual(expected, actual)

    def test_get_skill_list_shield_contains_desc_key(self):
        result = skill_list("shield")
        self.assertIn("desc", result)

    def test_get_skill_list_shield_desc_value_is_a_string(self):
        result = skill_list("shield")
        actual = result["desc"]
        expected = "Uses the characters full DEF to negate oncoming damage.\n"
        self.assertEqual(expected, actual)

    def test_get_skill_list_shield_contains_cost_key(self):
        result = skill_list("shield")
        self.assertIn("cost", result)

    def test_get_skill_list_shield_cost_value_is_2(self):
        result = skill_list("shield")
        actual = result["cost"]
        expected = 2
        self.assertEqual(expected, actual)

    def test_get_skill_list_contains_shield_bash_key(self):
        result = skill_list()
        self.assertIn("shield bash", result)

    def test_get_skill_list_shield_bash_contains_name_key(self):
        result = skill_list("shield bash")
        self.assertIn("name", result)

    def test_get_skill_list_shield_bash_name_value_is_shield_bash(self):
        result = skill_list("shield bash")
        actual = result["name"]
        expected = "shield bash"
        self.assertEqual(expected, actual)

    def test_get_skill_list_shield_bash_contains_desc_key(self):
        result = skill_list("shield bash")
        self.assertIn("desc", result)

    def test_get_skill_list_shield_bash_desc_value_is_a_string(self):
        result = skill_list("shield bash")
        actual = result["desc"]
        expected = ("Attacks with your shield, allowing you to both \n"
                    "attack and defend simultaneously.\n")
        self.assertEqual(expected, actual)

    def test_get_skill_list_shield_bash_contains_cost_key(self):
        result = skill_list("shield bash")
        self.assertIn("cost", result)

    def test_get_skill_list_shield_bash_cost_value_is_5(self):
        result = skill_list("shield bash")
        actual = result["cost"]
        expected = 5
        self.assertEqual(expected, actual)

    def test_get_skill_list_contains_battle_cry_key(self):
        result = skill_list()
        self.assertIn("battle cry", result)

    def test_get_skill_list_battle_cry_contains_name_key(self):
        result = skill_list("battle cry")
        self.assertIn("name", result)

    def test_get_skill_list_battle_cry_name_value_is_battle_cry(self):
        result = skill_list("battle cry")
        actual = result["name"]
        expected = "battle cry"
        self.assertEqual(expected, actual)

    def test_get_skill_list_battle_cry_contains_desc_key(self):
        result = skill_list("battle cry")
        self.assertIn("desc", result)

    def test_get_skill_list_battle_cry_desc_value_is_a_string(self):
        result = skill_list("battle cry")
        actual = result["desc"]
        expected = "Scares your enemy into lowering their DEF.\n"
        self.assertEqual(expected, actual)

    def test_get_skill_list_battle_cry_contains_cost_key(self):
        result = skill_list("battle cry")
        self.assertIn("cost", result)

    def test_get_skill_list_battle_cry_cost_value_is_3(self):
        result = skill_list("battle cry")
        actual = result["cost"]
        expected = 3
        self.assertEqual(expected, actual)

    def test_get_skill_list_contains_sharper_edge_key(self):
        result = skill_list()
        self.assertIn("sharper edge", result)

    def test_get_skill_list_sharper_edge_contains_name_key(self):
        result = skill_list("sharper edge")
        self.assertIn("name", result)

    def test_get_skill_list_sharper_edge_name_value_is_sharper_edge(self):
        result = skill_list("sharper edge")
        actual = result["name"]
        expected = "sharper edge"
        self.assertEqual(expected, actual)

    def test_get_skill_list_sharper_edge_contains_desc_key(self):
        result = skill_list("sharper edge")
        self.assertIn("desc", result)

    def test_get_skill_list_sharper_edge_desc_value_is_a_string(self):
        result = skill_list("sharper edge")
        actual = result["desc"]
        expected = ("You sharpen your weapon to a lethal point, \n"
                    "increasing your ATK.\n")
        self.assertEqual(expected, actual)

    def test_get_skill_list_sharper_edge_contains_cost_key(self):
        result = skill_list("sharper edge")
        self.assertIn("cost", result)

    def test_get_skill_list_sharper_edge_cost_value_is_3(self):
        result = skill_list("sharper edge")
        actual = result["cost"]
        expected = 3
        self.assertEqual(expected, actual)

    def test_get_skill_list_contains_focus_attack_key(self):
        result = skill_list()
        self.assertIn("focus attack", result)

    def test_get_skill_list_focus_attack_contains_name_key(self):
        result = skill_list("focus attack")
        self.assertIn("name", result)

    def test_get_skill_list_focus_attack_name_value_is_focus_attack(self):
        result = skill_list("focus attack")
        actual = result["name"]
        expected = "focus attack"
        self.assertEqual(expected, actual)

    def test_get_skill_list_focus_attack_contains_desc_key(self):
        result = skill_list("focus attack")
        self.assertIn("desc", result)

    def test_get_skill_list_focus_attack_desc_value_is_a_string(self):
        result = skill_list("focus attack")
        actual = result["desc"]
        expected = ("You focus solely on attacking your enemy, \n"
                    "increasing your LUK (Crit Chance) while launching \n"
                    "an attack.\n")
        self.assertEqual(expected, actual)

    def test_get_skill_list_focus_attack_contains_cost_key(self):
        result = skill_list("focus attack")
        self.assertIn("cost", result)

    def test_get_skill_list_focus_attack_cost_value_is_5(self):
        result = skill_list("focus attack")
        actual = result["cost"]
        expected = 5
        self.assertEqual(expected, actual)

    def test_get_skill_list_contains_haste_key(self):
        result = skill_list()
        self.assertIn("haste", result)

    def test_get_skill_list_haste_contains_name_key(self):
        result = skill_list("haste")
        self.assertIn("name", result)

    def test_get_skill_list_haste_name_value_is_haste(self):
        result = skill_list("haste")
        actual = result["name"]
        expected = "haste"
        self.assertEqual(expected, actual)

    def test_get_skill_list_haste_contains_desc_key(self):
        result = skill_list("haste")
        self.assertIn("desc", result)

    def test_get_skill_list_haste_desc_value_is_a_string(self):
        result = skill_list("haste")
        actual = result["desc"]
        expected = "You focus on quickening your steps, increasing you AGI.\n"
        self.assertEqual(expected, actual)

    def test_get_skill_list_haste_contains_cost_key(self):
        result = skill_list("haste")
        self.assertIn("cost", result)

    def test_get_skill_list_haste_cost_value_is_2(self):
        result = skill_list("haste")
        actual = result["cost"]
        expected = 2
        self.assertEqual(expected, actual)

    def test_get_skill_list_contains_fireball_key(self):
        result = skill_list()
        self.assertIn("fireball", result)

    def test_get_skill_list_fireball_contains_name_key(self):
        result = skill_list("fireball")
        self.assertIn("name", result)

    def test_get_skill_list_fireball_name_value_is_fireball(self):
        result = skill_list("fireball")
        actual = result["name"]
        expected = "fireball"
        self.assertEqual(expected, actual)

    def test_get_skill_list_fireball_contains_desc_key(self):
        result = skill_list("fireball")
        self.assertIn("desc", result)

    def test_get_skill_list_fireball_desc_value_is_a_string(self):
        result = skill_list("fireball")
        actual = result["desc"]
        expected = ("Send scorching projectiles towards your enemy, \n"
                    "dealing continuous damage as it continues to burn.\n")
        self.assertEqual(expected, actual)

    def test_get_skill_list_fireball_contains_cost_key(self):
        result = skill_list("fireball")
        self.assertIn("cost", result)

    def test_get_skill_list_fireball_cost_value_is_5(self):
        result = skill_list("fireball")
        actual = result["cost"]
        expected = 5
        self.assertEqual(expected, actual)

    def test_get_skill_list_contains_freezing_touch_key(self):
        result = skill_list()
        self.assertIn("freezing touch", result)

    def test_get_skill_list_freezing_touch_contains_name_key(self):
        result = skill_list("freezing touch")
        self.assertIn("name", result)

    def test_get_skill_list_freezing_touch_name_value_is_freezing_touch(self):
        result = skill_list("freezing touch")
        actual = result["name"]
        expected = "freezing touch"
        self.assertEqual(expected, actual)

    def test_get_skill_list_freezing_touch_contains_desc_key(self):
        result = skill_list("freezing touch")
        self.assertIn("desc", result)

    def test_get_skill_list_freezing_touch_desc_value_is_a_string(self):
        result = skill_list("freezing touch")
        actual = result["desc"]
        expected = ("Slow your enemies with a chilling touch, lowering \n"
                    "their AGI.\n")
        self.assertEqual(expected, actual)

    def test_get_skill_list_freezing_touch_contains_cost_key(self):
        result = skill_list("freezing touch")
        self.assertIn("cost", result)

    def test_get_skill_list_freezing_touch_cost_value_is_3(self):
        result = skill_list("freezing touch")
        actual = result["cost"]
        expected = 3
        self.assertEqual(expected, actual)

    def test_get_skill_list_contains_healing_light_key(self):
        result = skill_list()
        self.assertIn("healing light", result)

    def test_get_skill_list_healing_light_contains_name_key(self):
        result = skill_list("healing light")
        self.assertIn("name", result)

    def test_get_skill_list_healing_light_name_value_is_healing_light(self):
        result = skill_list("healing light")
        actual = result["name"]
        expected = "healing light"
        self.assertEqual(expected, actual)

    def test_get_skill_list_healing_light_contains_desc_key(self):
        result = skill_list("healing light")
        self.assertIn("desc", result)

    def test_get_skill_list_healing_light_desc_value_is_a_string(self):
        result = skill_list("healing light")
        actual = result["desc"]
        expected = ("A warm light envelops your wounds, healing you \n"
                    "slightly.\n")
        self.assertEqual(expected, actual)

    def test_get_skill_list_healing_light_contains_cost_key(self):
        result = skill_list("healing light")
        self.assertIn("cost", result)

    def test_get_skill_list_healing_light_cost_value_is_5(self):
        result = skill_list("healing light")
        actual = result["cost"]
        expected = 5
        self.assertEqual(expected, actual)
