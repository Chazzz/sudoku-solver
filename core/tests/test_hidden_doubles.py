import unittest
from core.rules.hidden_doubles import HiddenDoubles
from core.board import Board

class TestHiddenDoubles(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.rule = HiddenDoubles()
    
    def test_hidden_box(self):
        for c in self.board:
            if c.x < 3 and c.y < 3 and not (str(c) in ["A1", "C3"]):
                c.candidates = list(range(1,8))  # missing 8, 9
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 2)
        for e in update.eliminations:
            self.assertTrue(str(e) in ["A1", "C3"])
            self.assertEqual(e.candidates, list(range(1,8)))
        self.assertEqual(update.rule_name, "Hidden Doubles")
        self.assertEqual(update.explanation, "Given 8 and 9 are only possible in A1 and C3 for all cells in that box, those cell must be 8 and 9.")

    def test_hidden_row(self):
        for c in self.board:
            if c.y == 0 and not (str(c) in ["A1", "D1"]):
                c.candidates = list(range(1,8))  # missing 8, 9
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 2)
        for e in update.eliminations:
            self.assertTrue(str(e) in ["A1", "D1"])
            self.assertEqual(e.candidates, list(range(1,8)))
        self.assertEqual(update.rule_name, "Hidden Doubles")
        self.assertEqual(update.explanation, "Given 8 and 9 are only possible in A1 and D1 for all cells in that row, those cell must be 8 and 9.")

    def test_hidden_col(self):
        for c in self.board:
            if c.x == 0 and not (str(c) in ["A1", "A4"]):
                c.candidates = list(range(1,8))  # missing 8, 9
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 2)
        for e in update.eliminations:
            self.assertTrue(str(e) in ["A1", "A4"])
            self.assertEqual(e.candidates, list(range(1,8)))
        self.assertEqual(update.rule_name, "Hidden Doubles")
        self.assertEqual(update.explanation, "Given 8 and 9 are only possible in A1 and A4 for all cells in that column, those cell must be 8 and 9.")
