import unittest
from core.rules.hidden_singles import HiddenSingles
from core.board import Board

class TestHiddenSingles(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.rule = HiddenSingles()
    
    def test_hidden_box(self):
        for c in self.board:
            if c.x < 3 and c.y < 3 and not (c.x == 0 and c.y == 0):
                c.candidates = list(range(1,9)) # missing 9
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1)
        for e in update.eliminations:
            self.assertEqual(str(e), "A1")
            self.assertEqual(e.candidates, list(range(1,9)))
        self.assertEqual(update.rule_name, "Hidden Singles")
        self.assertEqual(update.explanation, "Given 9 is only possible in A1 for all cells in that box, that cell must be 9.")

    
    def test_hidden_row(self):
        for c in self.board:
            if c.y == 0 and not (c.x == 0 and c.y == 0):
                c.candidates = list(range(1,9)) # missing 9
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1)
        for e in update.eliminations:
            self.assertEqual(str(e), "A1")
            self.assertEqual(e.candidates, list(range(1,9)))
        self.assertEqual(update.rule_name, "Hidden Singles")
        self.assertEqual(update.explanation, "Given 9 is only possible in A1 for all cells in that row, that cell must be 9.")

    def test_hidden_col(self):
        for c in self.board:
            if c.x == 0 and not (c.x == 0 and c.y == 0):
                c.candidates = list(range(1,9)) # missing 9
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1)
        for e in update.eliminations:
            self.assertEqual(str(e), "A1")
            self.assertEqual(e.candidates, list(range(1,9)))
        self.assertEqual(update.rule_name, "Hidden Singles")
        self.assertEqual(update.explanation, "Given 9 is only possible in A1 for all cells in that column, that cell must be 9.")
