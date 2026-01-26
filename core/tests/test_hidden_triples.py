import unittest
from core.rules.hidden_triples import HiddenTriples
from core.board import Board

class TestHiddenDoubles(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.rule = HiddenTriples()
    
    def test_hidden_box(self):
        for c in self.board:
            if c.x < 3 and c.y < 3 and not (str(c) in ["A1", "B2", "C3"]):
                c.candidates = list(range(1,7))  # missing 7, 8, 9
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 3)
        for e in update.eliminations:
            self.assertTrue(str(e) in ["A1", "B2", "C3"])
            self.assertEqual(e.candidates, list(range(1,7)))
        self.assertEqual(update.rule_name, "Hidden Triples")
        self.assertEqual(update.explanation, "Given 7, 8, and 9 are only possible in A1, B2, and C3 for all cells in that box, those cell must be 7, 8, and 9.")

    def test_hidden_box_partial(self):
        for c in self.board:
            if c.x < 3 and c.y < 3 and not (str(c) in ["A1", "B2", "C3"]):
                c.candidates = list(range(1,7))  # missing 7, 8, 9
            if str(c) == "A1":
                c.candidates = [7, 8, 9]
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 2)
        for e in update.eliminations:
            self.assertTrue(str(e) in ["B2", "C3"])
            self.assertEqual(e.candidates, list(range(1,7)))
        self.assertEqual(update.rule_name, "Hidden Triples")
        self.assertEqual(update.explanation, "Given 7, 8, and 9 are only possible in A1, B2, and C3 for all cells in that box, those cell must be 7, 8, and 9.")


    def test_hidden_row(self):
        for c in self.board:
            if c.y == 0 and not (str(c) in ["A1", "D1", "E1"]):
                c.candidates = list(range(1,7))  # missing 7, 8, 9
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 3)
        for e in update.eliminations:
            self.assertTrue(str(e) in ["A1", "D1", "E1"])
            self.assertEqual(e.candidates, list(range(1,7)))
        self.assertEqual(update.rule_name, "Hidden Triples")
        self.assertEqual(update.explanation, "Given 7, 8, and 9 are only possible in A1, D1, and E1 for all cells in that row, those cell must be 7, 8, and 9.")

    def test_hidden_col(self):
        for c in self.board:
            if c.x == 0 and not (str(c) in ["A1", "A4", "A5"]):
                c.candidates = list(range(1,7))  # missing 7, 8, 9
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 3)
        for e in update.eliminations:
            self.assertTrue(str(e) in ["A1", "A4", "A5"])
            self.assertEqual(e.candidates, list(range(1,7)))
        self.assertEqual(update.rule_name, "Hidden Triples")
        self.assertEqual(update.explanation, "Given 7, 8, and 9 are only possible in A1, A4, and A5 for all cells in that column, those cell must be 7, 8, and 9.")
