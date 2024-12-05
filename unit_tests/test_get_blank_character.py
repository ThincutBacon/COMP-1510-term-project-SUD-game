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

    def test_get_blank_character_continuous_damage_contains_effect_key(self):
        result = blank_character()["continuous_damage"]
        self.assertIn("effect", result)

    def test_get_blank_character_continuous_damage_contains_time_key(self):
        result = blank_character()["continuous_damage"]
        self.assertIn("time", result)

    def test_get_blank_character_continuous_damage_effect_value_is_0(self):
        result = blank_character()["continuous_damage"]
        actual = result["effect"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_continuous_damage_time_value_is_0(self):
        result = blank_character()["continuous_damage"]
        actual = result["time"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_ATK_value_is_0(self):
        result = blank_character()
        actual = result["ATK"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_DEF_value_is_0(self):
        result = blank_character()
        actual = result["DEF"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_AGI_value_is_0(self):
        result = blank_character()
        actual = result["AGI"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_LUK_value_is_0(self):
        result = blank_character()
        actual = result["LUK"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_buff_contains_ATK_key(self):
        result = blank_character()["buff"]
        self.assertIn("ATK", result)

    def test_get_blank_character_buff_ATK_contains_effect_key(self):
        result = blank_character()["buff"]["ATK"]
        self.assertIn("effect", result)

    def test_get_blank_character_buff_ATK_contains_time_key(self):
        result = blank_character()["buff"]["ATK"]
        self.assertIn("time", result)

    def test_get_blank_character_buff_ATK_effect_value_is_0(self):
        result = blank_character()["buff"]["ATK"]
        actual = result["effect"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_buff_ATK_time_value_is_0(self):
        result = blank_character()["buff"]["ATK"]
        actual = result["time"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_buff_contains_DEF_key(self):
        result = blank_character()["buff"]
        self.assertIn("DEF", result)

    def test_get_blank_character_buff_DEF_contains_effect_key(self):
        result = blank_character()["buff"]["DEF"]
        self.assertIn("effect", result)

    def test_get_blank_character_buff_DEF_contains_time_key(self):
        result = blank_character()["buff"]["DEF"]
        self.assertIn("time", result)

    def test_get_blank_character_buff_DEF_effect_value_is_0(self):
        result = blank_character()["buff"]["DEF"]
        actual = result["effect"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_buff_DEF_time_value_is_0(self):
        result = blank_character()["buff"]["DEF"]
        actual = result["time"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_buff_contains_AGI_key(self):
        result = blank_character()["buff"]
        self.assertIn("AGI", result)

    def test_get_blank_character_buff_AGI_contains_effect_key(self):
        result = blank_character()["buff"]["AGI"]
        self.assertIn("effect", result)

    def test_get_blank_character_buff_AGI_contains_time_key(self):
        result = blank_character()["buff"]["AGI"]
        self.assertIn("time", result)

    def test_get_blank_character_buff_AGI_effect_value_is_0(self):
        result = blank_character()["buff"]["AGI"]
        actual = result["effect"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_buff_AGI_time_value_is_0(self):
        result = blank_character()["buff"]["AGI"]
        actual = result["time"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_buff_contains_LUK_key(self):
        result = blank_character()["buff"]
        self.assertIn("LUK", result)

    def test_get_blank_character_buff_LUK_contains_effect_key(self):
        result = blank_character()["buff"]["LUK"]
        self.assertIn("effect", result)

    def test_get_blank_character_buff_LUK_contains_time_key(self):
        result = blank_character()["buff"]["LUK"]
        self.assertIn("time", result)

    def test_get_blank_character_buff_LUK_effect_value_is_0(self):
        result = blank_character()["buff"]["LUK"]
        actual = result["effect"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_buff_LUK_time_value_is_0(self):
        result = blank_character()["buff"]["LUK"]
        actual = result["time"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_debuff_contains_ATK_key(self):
        result = blank_character()["debuff"]
        self.assertIn("ATK", result)

    def test_get_blank_character_debuff_ATK_contains_effect_key(self):
        result = blank_character()["debuff"]["ATK"]
        self.assertIn("effect", result)

    def test_get_blank_character_debuff_ATK_contains_time_key(self):
        result = blank_character()["debuff"]["ATK"]
        self.assertIn("time", result)

    def test_get_blank_character_debuff_ATK_effect_value_is_0(self):
        result = blank_character()["debuff"]["ATK"]
        actual = result["effect"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_debuff_ATK_time_value_is_0(self):
        result = blank_character()["debuff"]["ATK"]
        actual = result["time"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_debuff_contains_DEF_key(self):
        result = blank_character()["debuff"]
        self.assertIn("DEF", result)

    def test_get_blank_character_debuff_DEF_contains_effect_key(self):
        result = blank_character()["debuff"]["DEF"]
        self.assertIn("effect", result)

    def test_get_blank_character_debuff_DEF_contains_time_key(self):
        result = blank_character()["debuff"]["DEF"]
        self.assertIn("time", result)

    def test_get_blank_character_debuff_DEF_effect_value_is_0(self):
        result = blank_character()["debuff"]["DEF"]
        actual = result["effect"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_debuff_DEF_time_value_is_0(self):
        result = blank_character()["debuff"]["DEF"]
        actual = result["time"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_debuff_contains_AGI_key(self):
        result = blank_character()["debuff"]
        self.assertIn("AGI", result)

    def test_get_blank_character_debuff_AGI_contains_effect_key(self):
        result = blank_character()["debuff"]["AGI"]
        self.assertIn("effect", result)

    def test_get_blank_character_debuff_AGI_contains_time_key(self):
        result = blank_character()["debuff"]["AGI"]
        self.assertIn("time", result)

    def test_get_blank_character_debuff_AGI_effect_value_is_0(self):
        result = blank_character()["debuff"]["AGI"]
        actual = result["effect"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_debuff_AGI_time_value_is_0(self):
        result = blank_character()["debuff"]["AGI"]
        actual = result["time"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_debuff_contains_LUK_key(self):
        result = blank_character()["debuff"]
        self.assertIn("LUK", result)

    def test_get_blank_character_debuff_LUK_contains_effect_key(self):
        result = blank_character()["debuff"]["LUK"]
        self.assertIn("effect", result)

    def test_get_blank_character_debuff_LUK_contains_time_key(self):
        result = blank_character()["debuff"]["LUK"]
        self.assertIn("time", result)

    def test_get_blank_character_debuff_LUK_effect_value_is_0(self):
        result = blank_character()["debuff"]["LUK"]
        actual = result["effect"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_debuff_LUK_time_value_is_0(self):
        result = blank_character()["debuff"]["LUK"]
        actual = result["time"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_modifier_contains_ATK_key(self):
        result = blank_character()["modifier"]
        self.assertIn("ATK", result)

    def test_get_blank_character_modifier_ATK_value_is_0(self):
        result = blank_character()["modifier"]
        actual = result["ATK"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_modifier_contains_DEF_key(self):
        result = blank_character()["modifier"]
        self.assertIn("DEF", result)

    def test_get_blank_character_modifier_DEF_value_is_0(self):
        result = blank_character()["modifier"]
        actual = result["DEF"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_equipment_contains_armour_key(self):
        result = blank_character()["equipment"]
        self.assertIn("armour", result)

    def test_get_blank_character_equipment_contains_weapon_key(self):
        result = blank_character()["equipment"]
        self.assertIn("weapon", result)

    def test_get_blank_character_x_coordinate_value_is_0(self):
        result = blank_character()
        actual = result["x-coordinate"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_y_coordinate_value_is_0(self):
        result = blank_character()
        actual = result["y-coordinate"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_blank_character_gold_value_is_0(self):
        result = blank_character()
        actual = result["gold"]
        expected = 0
        self.assertEqual(expected, actual)

