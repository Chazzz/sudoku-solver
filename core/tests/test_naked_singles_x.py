import unittest
from core.rules.naked_singles_x import NakedSinglesX
from core.board import Board

class TestNakedSinglesX(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.rule = NakedSinglesX()
        self.board.is_x = True
    
    def test_eq(self):
        golden_coordinates = ['B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8', 'I9']
        for c in self.board:
            if c.x == 0 and c.y == 0:
                c.candidates = [1]
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 8)
        for e in update.eliminations:
            self.assertTrue(str(e) in golden_coordinates)
            self.assertEqual(e.candidates, [1])
        self.assertEqual(update.rule_name, "Naked Singles X")
        self.assertEqual(update.explanation, "Given A1 can only be 1, no cell in same diagonal can also be 1.")

    def test_plus(self):
        golden_coordinates = ['A9', 'B8', 'C7', 'D6', 'E5', 'F4', 'G3', 'H2']
        for c in self.board:
            if c.x == 8 and c.y == 0:
                c.candidates = [1]
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 8)
        for e in update.eliminations:
            self.assertTrue(str(e) in golden_coordinates)
            self.assertEqual(e.candidates, [1])
        self.assertEqual(update.rule_name, "Naked Singles X")
        self.assertEqual(update.explanation, "Given I1 can only be 1, no cell in same diagonal can also be 1.")

    def test_x(self):
        golden_coordinates = ['A1', 'B2', 'C3', 'D4', 'F6', 'G7', 'H8', 'I9', 'A9', 'B8', 'C7', 'D6', 'F4', 'G3', 'H2', 'I1']
        for c in self.board:
            if c.x == 4 and c.y == 4:
                c.candidates = [1]
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 16)
        for e in update.eliminations:
            self.assertTrue(str(e) in golden_coordinates)
            self.assertEqual(e.candidates, [1])
        self.assertEqual(update.rule_name, "Naked Singles X")
        self.assertEqual(update.explanation, "Given E5 can only be 1, no cell in same diagonal can also be 1.")
