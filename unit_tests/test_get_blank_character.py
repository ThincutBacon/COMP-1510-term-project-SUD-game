from unittest import TestCase

from modules.get import blank_character


class TestGetBlankCharacter(TestCase):

    def test_get_blank_character_contains_kingdom_key(self):
        result = blank_character()
        self.assertIn("kingdom", result)

    def test_get_blank_character_contains_name_key(self):
        result = blank_character()
        self.assertIn("name", result)

    def test_get_blank_character_contains_species_key(self):
        result = blank_character()
        self.assertIn("species", result)

    def test_get_blank_character_contains_species_adjective_key(self):
        result = blank_character()
        self.assertIn("species_adjective", result)

    def test_get_blank_character_contains_skill_class_key(self):
        result = blank_character()
        self.assertIn("skill_class", result)

    def test_get_blank_character_contains_LVL_key(self):
        result = blank_character()
        self.assertIn("LVL", result)

    def test_get_blank_character_contains_EXP_key(self):
        result = blank_character()
        self.assertIn("EXP", result)

    def test_get_blank_character_contains_max_HP_key(self):
        result = blank_character()
        self.assertIn("max_HP", result)

    def test_get_blank_character_contains_current_HP_key(self):
        result = blank_character()
        self.assertIn("current_HP", result)

    def test_get_blank_character_contains_max_SP_key(self):
        result = blank_character()
        self.assertIn("max_SP", result)

    def test_get_blank_character_contains_current_SP_key(self):
        result = blank_character()
        self.assertIn("current_SP", result)

    def test_get_blank_character_contains_reduce_damage_key(self):
        result = blank_character()
        self.assertIn("reduce_damage", result)

    def test_get_blank_character_contains_continuous_damage_key(self):
        result = blank_character()
        self.assertIn("continuous_damage", result)

    def test_get_blank_character_contains_ATK_key(self):
        result = blank_character()
        self.assertIn("ATK", result)

    def test_get_blank_character_contains_DEF_key(self):
        result = blank_character()
        self.assertIn("DEF", result)

    def test_get_blank_character_contains_AGI_key(self):
        result = blank_character()
        self.assertIn("AGI", result)

    def test_get_blank_character_contains_LUK_key(self):
        result = blank_character()
        self.assertIn("LUK", result)

    def test_get_blank_character_contains_buff_key(self):
        result = blank_character()
        self.assertIn("buff", result)

    def test_get_blank_character_contains_debuff_key(self):
        result = blank_character()
        self.assertIn("debuff", result)

    def test_get_blank_character_contains_modifier_key(self):
        result = blank_character()
        self.assertIn("modifier", result)

    def test_get_blank_character_contains_equipment_key(self):
        result = blank_character()
        self.assertIn("equipment", result)

    def test_get_blank_character_contains_inventory_key(self):
        result = blank_character()
        self.assertIn("inventory", result)

    def test_get_blank_character_contains_x_coordinate_key(self):
        result = blank_character()
        self.assertIn("x-coordinate", result)

    def test_get_blank_character_contains_y_coordinate_key(self):
        result = blank_character()
        self.assertIn("y-coordinate", result)

    def test_get_blank_character_contains_gold_key(self):
        result = blank_character()
        self.assertIn("gold", result)

    def test_get_blank_character_LVL_value_is_1(self):
        result = blank_character()
        actual = result["LVL"]
        expected = 1
        self.assertEqual(expected, actual)

    def test_get_blank_character_EXP_value_is_20(self):
        result = blank_character()
        actual = result["EXP"]
        expected = 20
        self.assertEqual(expected, actual)

    def test_get_blank_character_max_HP_value_is_0(self):
        result = blank_character()
        actual = result["max_HP"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_current_HP_value_is_0(self):
        result = blank_character()
        actual = result["current_HP"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_max_SP_value_is_0(self):
        result = blank_character()
        actual = result["max_SP"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_current_SP_value_is_0(self):
        result = blank_character()
        actual = result["current_SP"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_reduce_damage_value_is_0(self):
        result = blank_character()
        actual = result["reduce_damage"]
        expected = 0
        self.assertEqual(expected, actual)






    def test_get_blank_character_contains_continuous_damage_key(self):
        result = blank_character()
        self.assertIn("continuous_damage", result)

    def test_get_blank_character_contains_ATK_key(self):
        result = blank_character()
        self.assertIn("ATK", result)

    def test_get_blank_character_contains_DEF_key(self):
        result = blank_character()
        self.assertIn("DEF", result)

    def test_get_blank_character_contains_AGI_key(self):
        result = blank_character()
        self.assertIn("AGI", result)

    def test_get_blank_character_contains_LUK_key(self):
        result = blank_character()
        self.assertIn("LUK", result)

    def test_get_blank_character_contains_buff_key(self):
        result = blank_character()
        self.assertIn("buff", result)

    def test_get_blank_character_contains_debuff_key(self):
        result = blank_character()
        self.assertIn("debuff", result)

    def test_get_blank_character_contains_modifier_key(self):
        result = blank_character()
        self.assertIn("modifier", result)

    def test_get_blank_character_contains_equipment_key(self):
        result = blank_character()
        self.assertIn("equipment", result)

    def test_get_blank_character_contains_inventory_key(self):
        result = blank_character()
        self.assertIn("inventory", result)

    def test_get_blank_character_contains_x_coordinate_key(self):
        result = blank_character()
        self.assertIn("x-coordinate", result)

    def test_get_blank_character_contains_y_coordinate_key(self):
        result = blank_character()
        self.assertIn("y-coordinate", result)

    def test_get_blank_character_contains_gold_key(self):
        result = blank_character()
        self.assertIn("gold", result)



    def test_make_character_x_coordinate_value_is_0(self):
        result = make_character()
        actual = result["X-coordinate"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_make_character_y_coordinate_value_is_0(self):
        result = make_character()
        actual = result["Y-coordinate"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_make_character_current_HP_value_is_5(self):
        result = make_character()
        actual = result["Current HP"]
        expected = 5
        self.assertEqual(expected, actual)
