import unittest
from core.rules.box_reduction import BoxReduction
from core.board import Board

class TestBoxReduction(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.rule = BoxReduction()

    def test_box_reduction_via_row(self):
        golden_coordinates = ['A1', 'A3', 'B1', 'B3', 'C1', 'C3']
        for c in self.board:
            if c.y in [1] and c.x not in [0, 1]:
                c.candidates = list(range(1,9)) # missing 9
        update = self.rule.find_update(self.board)
        for e in update.eliminations:
            self.assertTrue(str(e) in golden_coordinates)
            self.assertEqual(e.candidates, [9])
        self.assertEqual(update.rule_name, "Box Reduction")
        self.assertEqual(update.explanation, "Row 2 can only be 9 inside box (0, 0), so no other cells in that box can be that value.")

    def test_box_reduction_via_row(self):
        golden_coordinates = ['D4', 'D5', 'D6', 'F4', 'F5', 'F6']
        for c in self.board:
            if c.y not in [3, 4, 5] and c.x in [4]:
                c.candidates = list(range(1,9)) # missing 9
        update = self.rule.find_update(self.board)
        for e in update.eliminations:
            self.assertTrue(str(e) in golden_coordinates)
            self.assertEqual(e.candidates, [9])
        self.assertEqual(update.rule_name, "Box Reduction")
        self.assertEqual(update.explanation, "Column E can only be 9 inside box (1, 1), so no other cells in that box can be that value.")