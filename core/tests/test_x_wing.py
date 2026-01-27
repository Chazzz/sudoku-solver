import unittest
from core.rules.x_wing import XWing
from core.board import Board

class TestXWing(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.rule = XWing()

    def test_xwing_rows(self):
        for c in self.board:
            if c.y in [0, 5] and not (str(c) in ["A1", "D1", "A6", "D6"]):
                c.candidates = list(range(1,9))  # missing 9
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 14)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['A2', 'D2', 'A3', 'D3', 'A4', 'D4', 'A5', 'D5', 'A7', 'D7', 'A8', 'D8', 'A9', 'D9'])
            self.assertEqual(e.candidates, [9])
        self.assertEqual(update.rule_name, "X Wing")
        self.assertEqual(update.explanation, "Two rows can only place 9 in column A and D. Therefore no other row can place 9 in column A and D.")

    def test_xwing_cols(self):
        for c in self.board:
            if c.x in [0, 5] and not (str(c) in ["A1", "F1", "A6", "F6"]):
                c.candidates = list(range(1,9))  # missing 9
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 14)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['B1', 'B6', 'C1', 'C6', 'D1', 'D6', 'E1', 'E6', 'G1', 'G6', 'H1', 'H6', 'I1', 'I6'])
            self.assertEqual(e.candidates, [9])
        self.assertEqual(update.rule_name, "X Wing")
        self.assertEqual(update.explanation, "Two columns can only place 9 in row 1 and 6. Therefore no other column can place 9 in row 1 and 6.")