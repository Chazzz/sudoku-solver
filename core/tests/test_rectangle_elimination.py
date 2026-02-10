import unittest
from core.rules.rectangle_elimination import RectangleElimination
from core.board import Board

class TestRectangleElimination(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.rule = RectangleElimination()

    def test_rectangle_elimination_rows(self):
        for c in self.board:
            if c.y in [0] and not (str(c) in ["A1", "D1"]):
                c.candidates = list(range(1,9))  # missing 9
            if str(c) in ["D5", "D6", "E5", "E6", "F4", "F5", "F6"]:
                c.candidates = list(range(1,9))  # missing 9
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['A4'])
            self.assertEqual(e.candidates, [9])
        self.assertEqual(update.rule_name, "Rectangle Elimination")
        self.assertEqual(update.explanation, "Row 1 can only place 9 in cells A1 and D1. Therefore any cell in the same column as A1 cannot eliminate all candidates in a box with conjunction with D1.")

    def test_rectangle_elimination_cols(self):
        for c in self.board:
            if c.x in [0] and not (str(c) in ["A1", "A4"]):
                c.candidates = list(range(1,9))  # missing 9
            if str(c) in ["D6", "E5", "E6", "F4", "F5", "F6"]:
                c.candidates = list(range(1,9))  # missing 9
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['D1'])
            self.assertEqual(e.candidates, [9])
        self.assertEqual(update.rule_name, "Rectangle Elimination")
        self.assertEqual(update.explanation, "Col A can only place 9 in cells A1 and A4. Therefore any cell in the same row as A1 cannot eliminate all candidates in a box with conjunction with A4.")

