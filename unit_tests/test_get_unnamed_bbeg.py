from unittest import TestCase

from modules.get import unnamed_bbeg


class TestGetBlankCharacter(TestCase):

    def test_get_unnamed_bbeg_contains_name_key(self):
        result = unnamed_bbeg()
        self.assertIn("name", result)

    def test_get_unnamed_bbeg_contains_max_HP_key(self):
        result = unnamed_bbeg()
        self.assertIn("max_HP", result)

    def test_get_unnamed_bbeg_contains_current_HP_key(self):
        result = unnamed_bbeg()
        self.assertIn("current_HP", result)

    def test_get_unnamed_bbeg_contains_current_SP_key(self):
        result = unnamed_bbeg()
        self.assertIn("current_SP", result)

    def test_get_unnamed_bbeg_contains_reduce_damage_key(self):
        result = unnamed_bbeg()
        self.assertIn("reduce_damage", result)

    def test_get_unnamed_bbeg_contains_continuous_damage_key(self):
        result = unnamed_bbeg()
        self.assertIn("continuous_damage", result)

    def test_get_unnamed_bbeg_contains_ATK_key(self):
        result = unnamed_bbeg()
        self.assertIn("ATK", result)

    def test_get_unnamed_bbeg_contains_DEF_key(self):
        result = unnamed_bbeg()
        self.assertIn("DEF", result)

    def test_get_unnamed_bbeg_contains_AGI_key(self):
        result = unnamed_bbeg()
        self.assertIn("AGI", result)

    def test_get_unnamed_bbeg_contains_LUK_key(self):
        result = unnamed_bbeg()
        self.assertIn("LUK", result)

    def test_get_unnamed_bbeg_contains_actions_key(self):
        result = unnamed_bbeg()
        self.assertIn("actions", result)

    def test_get_unnamed_bbeg_contains_skill_key(self):
        result = unnamed_bbeg()
        self.assertIn("skill", result)

    def test_get_unnamed_bbeg_contains_EXP_key(self):
        result = unnamed_bbeg()
        self.assertIn("EXP", result)

    def test_get_unnamed_bbeg_contains_gold_key(self):
        result = unnamed_bbeg()
        self.assertIn("gold", result)

    def test_get_unnamed_bbeg_contains_buff_key(self):
        result = unnamed_bbeg()
        self.assertIn("buff", result)

    def test_get_unnamed_bbeg_contains_debuff_key(self):
        result = unnamed_bbeg()
        self.assertIn("debuff", result)

    def test_get_unnamed_bbeg_contains_modifier_key(self):
        result = unnamed_bbeg()
        self.assertIn("modifier", result)

    def test_get_unnamed_bbeg_max_HP_value_is_100(self):
        result = unnamed_bbeg()
        actual = result["max_HP"]
        expected = 100
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_current_HP_value_is_100(self):
        result = unnamed_bbeg()
        actual = result["current_HP"]
        expected = 100
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_current_SP_value_is_300(self):
        result = unnamed_bbeg()
        actual = result["current_SP"]
        expected = 300
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_reduce_damage_value_is_0(self):
        result = unnamed_bbeg()
        actual = result["reduce_damage"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_continuous_damage_contains_effect_key(self):
        result = unnamed_bbeg()["continuous_damage"]
        self.assertIn("effect", result)

    def test_get_unnamed_bbeg_continuous_damage_contains_time_key(self):
        result = unnamed_bbeg()["continuous_damage"]
        self.assertIn("time", result)

    def test_get_unnamed_bbeg_continuous_damage_effect_value_is_0(self):
        result = unnamed_bbeg()["continuous_damage"]
        actual = result["effect"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_continuous_damage_time_value_is_0(self):
        result = unnamed_bbeg()["continuous_damage"]
        actual = result["time"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_ATK_value_is_0(self):
        result = unnamed_bbeg()
        actual = result["ATK"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_DEF_value_is_0(self):
        result = unnamed_bbeg()
        actual = result["DEF"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_AGI_value_is_0(self):
        result = unnamed_bbeg()
        actual = result["AGI"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_LUK_value_is_0(self):
        result = unnamed_bbeg()
        actual = result["LUK"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_actions_value_is_correct(self):
        result = unnamed_bbeg()
        actual = result["actions"]
        expected = ["defend", "skill", "defend", "attack", "skill", "attack"]
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_skill_value_is_focus_attack(self):
        result = unnamed_bbeg()
        actual = result["skill"]
        expected = "focus attack"
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_EXP_value_is_100(self):
        result = unnamed_bbeg()
        actual = result["EXP"]
        expected = 100
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_gold_value_is_100(self):
        result = unnamed_bbeg()
        actual = result["gold"]
        expected = 100
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_buff_contains_ATK_key(self):
        result = unnamed_bbeg()["buff"]
        self.assertIn("ATK", result)

    def test_get_unnamed_bbeg_buff_ATK_contains_effect_key(self):
        result = unnamed_bbeg()["buff"]["ATK"]
        self.assertIn("effect", result)

    def test_get_unnamed_bbeg_buff_ATK_contains_time_key(self):
        result = unnamed_bbeg()["buff"]["ATK"]
        self.assertIn("time", result)

    def test_get_unnamed_bbeg_buff_ATK_effect_value_is_0(self):
        result = unnamed_bbeg()["buff"]["ATK"]
        actual = result["effect"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_buff_ATK_time_value_is_0(self):
        result = unnamed_bbeg()["buff"]["ATK"]
        actual = result["time"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_buff_contains_DEF_key(self):
        result = unnamed_bbeg()["buff"]
        self.assertIn("DEF", result)

    def test_get_unnamed_bbeg_buff_DEF_contains_effect_key(self):
        result = unnamed_bbeg()["buff"]["DEF"]
        self.assertIn("effect", result)

    def test_get_unnamed_bbeg_buff_DEF_contains_time_key(self):
        result = unnamed_bbeg()["buff"]["DEF"]
        self.assertIn("time", result)

    def test_get_unnamed_bbeg_buff_DEF_effect_value_is_0(self):
        result = unnamed_bbeg()["buff"]["DEF"]
        actual = result["effect"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_buff_DEF_time_value_is_0(self):
        result = unnamed_bbeg()["buff"]["DEF"]
        actual = result["time"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_buff_contains_AGI_key(self):
        result = unnamed_bbeg()["buff"]
        self.assertIn("AGI", result)

    def test_get_unnamed_bbeg_buff_AGI_contains_effect_key(self):
        result = unnamed_bbeg()["buff"]["AGI"]
        self.assertIn("effect", result)

    def test_get_unnamed_bbeg_buff_AGI_contains_time_key(self):
        result = unnamed_bbeg()["buff"]["AGI"]
        self.assertIn("time", result)

    def test_get_unnamed_bbeg_buff_AGI_effect_value_is_0(self):
        result = unnamed_bbeg()["buff"]["AGI"]
        actual = result["effect"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_buff_AGI_time_value_is_0(self):
        result = unnamed_bbeg()["buff"]["AGI"]
        actual = result["time"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_buff_contains_LUK_key(self):
        result = unnamed_bbeg()["buff"]
        self.assertIn("LUK", result)

    def test_get_unnamed_bbeg_buff_LUK_contains_effect_key(self):
        result = unnamed_bbeg()["buff"]["LUK"]
        self.assertIn("effect", result)

    def test_get_unnamed_bbeg_buff_LUK_contains_time_key(self):
        result = unnamed_bbeg()["buff"]["LUK"]
        self.assertIn("time", result)

    def test_get_unnamed_bbeg_buff_LUK_effect_value_is_0(self):
        result = unnamed_bbeg()["buff"]["LUK"]
        actual = result["effect"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_buff_LUK_time_value_is_0(self):
        result = unnamed_bbeg()["buff"]["LUK"]
        actual = result["time"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_debuff_contains_ATK_key(self):
        result = unnamed_bbeg()["debuff"]
        self.assertIn("ATK", result)

    def test_get_unnamed_bbeg_debuff_ATK_contains_effect_key(self):
        result = unnamed_bbeg()["debuff"]["ATK"]
        self.assertIn("effect", result)

    def test_get_unnamed_bbeg_debuff_ATK_contains_time_key(self):
        result = unnamed_bbeg()["debuff"]["ATK"]
        self.assertIn("time", result)

    def test_get_unnamed_bbeg_debuff_ATK_effect_value_is_0(self):
        result = unnamed_bbeg()["debuff"]["ATK"]
        actual = result["effect"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_debuff_ATK_time_value_is_0(self):
        result = unnamed_bbeg()["debuff"]["ATK"]
        actual = result["time"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_debuff_contains_DEF_key(self):
        result = unnamed_bbeg()["debuff"]
        self.assertIn("DEF", result)

    def test_get_unnamed_bbeg_debuff_DEF_contains_effect_key(self):
        result = unnamed_bbeg()["debuff"]["DEF"]
        self.assertIn("effect", result)

    def test_get_unnamed_bbeg_debuff_DEF_contains_time_key(self):
        result = unnamed_bbeg()["debuff"]["DEF"]
        self.assertIn("time", result)

    def test_get_unnamed_bbeg_debuff_DEF_effect_value_is_0(self):
        result = unnamed_bbeg()["debuff"]["DEF"]
        actual = result["effect"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_debuff_DEF_time_value_is_0(self):
        result = unnamed_bbeg()["debuff"]["DEF"]
        actual = result["time"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_debuff_contains_AGI_key(self):
        result = unnamed_bbeg()["debuff"]
        self.assertIn("AGI", result)

    def test_get_unnamed_bbeg_debuff_AGI_contains_effect_key(self):
        result = unnamed_bbeg()["debuff"]["AGI"]
        self.assertIn("effect", result)

    def test_get_unnamed_bbeg_debuff_AGI_contains_time_key(self):
        result = unnamed_bbeg()["debuff"]["AGI"]
        self.assertIn("time", result)

    def test_get_unnamed_bbeg_debuff_AGI_effect_value_is_0(self):
        result = unnamed_bbeg()["debuff"]["AGI"]
        actual = result["effect"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_debuff_AGI_time_value_is_0(self):
        result = unnamed_bbeg()["debuff"]["AGI"]
        actual = result["time"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_debuff_contains_LUK_key(self):
        result = unnamed_bbeg()["debuff"]
        self.assertIn("LUK", result)

    def test_get_unnamed_bbeg_debuff_LUK_contains_effect_key(self):
        result = unnamed_bbeg()["debuff"]["LUK"]
        self.assertIn("effect", result)

    def test_get_unnamed_bbeg_debuff_LUK_contains_time_key(self):
        result = unnamed_bbeg()["debuff"]["LUK"]
        self.assertIn("time", result)

    def test_get_unnamed_bbeg_debuff_LUK_effect_value_is_0(self):
        result = unnamed_bbeg()["debuff"]["LUK"]
        actual = result["effect"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_debuff_LUK_time_value_is_0(self):
        result = unnamed_bbeg()["debuff"]["LUK"]
        actual = result["time"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_modifier_contains_ATK_key(self):
        result = unnamed_bbeg()["modifier"]
        self.assertIn("ATK", result)

    def test_get_unnamed_bbeg_modifier_ATK_value_is_0(self):
        result = unnamed_bbeg()["modifier"]
        actual = result["ATK"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_unnamed_bbeg_modifier_contains_DEF_key(self):
        result = unnamed_bbeg()["modifier"]
        self.assertIn("DEF", result)

    def test_get_unnamed_bbeg_modifier_DEF_value_is_0(self):
        result = unnamed_bbeg()["modifier"]
        actual = result["DEF"]
        expected = 0
        self.assertEqual(expected, actual)