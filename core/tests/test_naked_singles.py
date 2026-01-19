import unittest
from core.rules.naked_singles import NakedSingles
from core.board import Board

class TestNakedSingles(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.rule = NakedSingles()
    
    def test_basic_case(self):
        golden_coordinates = ['B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'B2', 'B3', 'C2', 'C3']
        for c in self.board:
            if c.x == 0 and c.y == 0:
                c.candidates = [1]
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 20)
        for e in update.eliminations:
            self.assertTrue(str(e) in golden_coordinates)
            self.assertEqual(e.candidates, [1])
        self.assertEqual(update.rule_name, "Naked Singles")
        self.assertEqual(update.explanation, "Given A1 can only be 1, no cell in same row, column, or box can also be 1.")
