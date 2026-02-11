import unittest
from core.rules.w_wing import WWing
from core.board import Board

class TestWWing(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.rule = WWing()

    def test_wwing(self):
        for c in self.board:
            if c.y in [0, 5] and not (str(c) in ["A1", "D1", "A6", "E6"]):
                c.candidates = list(range(1,8))  # missing 8,9
            if c.x in [0] and not (str(c) in ["A1", "D1", "A6", "E6"]):
                c.candidates = list(range(1,8))  # missing 8,9
            if str(c) in ["A1", "D1", "A6", "E6"]:
                c.candidates = [8, 9]
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 4)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['D4', 'D5', 'E2', 'E3'])
            self.assertEqual(e.candidates, [8, 9])
        self.assertEqual(update.rule_name, "W Wing")
        self.assertEqual(update.explanation, "Mutualy exclusive pair (8, 9) forms a \"W\" at D1, A1, A6, and E6, eliminating 8 and 9 for a cell which sees both D1 and E6.")