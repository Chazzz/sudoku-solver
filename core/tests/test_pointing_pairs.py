import unittest
from core.rules.pointing_pairs import PointingPairs
from core.board import Board

class TestPointingPairs(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.rule = PointingPairs()

    def test_pointing_row(self):
        golden_coordinates = ['C4', 'C5', 'C6', 'C7', 'C8', 'C9']
        for c in self.board:
            if c.y in [0, 1, 2] and c.x in [0, 1]:
                c.candidates = list(range(1,9)) # missing 9
        update = self.rule.find_update(self.board)
        for e in update.eliminations:
            self.assertTrue(str(e) in golden_coordinates)
            self.assertEqual(e.candidates, [9])
        self.assertEqual(update.rule_name, "Pointing Pairs")
        self.assertEqual(update.explanation, "Box (0, 0) can only be 9 for cells C1, C2, and C3, no cell in same row outside that box can be that value.")

    def test_pointing_column(self):
        golden_coordinates = ['D1', 'E1', 'F1', 'G1', 'H1', 'I1']
        for c in self.board:
            if c.y in [1, 2] and c.x in [0, 1, 2]:
                c.candidates = list(range(1,9)) # missing 9
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 6)
        for e in update.eliminations:
            self.assertTrue(str(e) in golden_coordinates)
            self.assertEqual(e.candidates, [9])
        self.assertEqual(update.rule_name, "Pointing Pairs")
        self.assertEqual(update.explanation, "Box (0, 0) can only be 9 for cells A1, B1, and C1, no cell in same column outside that box can be that value.")