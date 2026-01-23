import unittest
from core.rules.naked_triples import NakedTriples
from core.board import Board

class TestNakedTriples(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.rule = NakedTriples()

    def test_naked_row(self):
        golden_coordinates = ['B2', 'C2', 'D2', 'G2', 'H2', 'I2']
        for c in self.board:
            if c.x == 0 and c.y == 1:
                c.candidates = [2, 8]
            if c.x == 4 and c.y == 1:
                c.candidates = [2, 5]
            if c.x == 5 and c.y == 1:
                c.candidates = [2, 5, 8]
        update = self.rule.find_update(self.board)
        for e in update.eliminations:
            self.assertTrue(str(e) in golden_coordinates)
            self.assertEqual(e.candidates, [2, 5, 8])
        self.assertEqual(update.rule_name, "Naked Triples")
        self.assertEqual(update.explanation, "Three cells A2, E2, and F2 have the same three candidates 2, 5, and 8, therefore no other cell in that row can have that value.")

    def test_naked_column(self):
        golden_coordinates = ['B2', 'B3', 'B4', 'B7', 'B8', 'B9']
        for c in self.board:
            if c.x == 1 and c.y == 0:
                c.candidates = [2, 8]
            if c.x == 1 and c.y == 4:
                c.candidates = [2, 5]
            if c.x == 1 and c.y == 5:
                c.candidates = [2, 5, 8]
        update = self.rule.find_update(self.board)
        for e in update.eliminations:
            self.assertTrue(str(e) in golden_coordinates)
            self.assertEqual(e.candidates, [2, 5, 8])
        self.assertEqual(update.rule_name, "Naked Triples")
        self.assertEqual(update.explanation, "Three cells B1, B5, and B6 have the same three candidates 2, 5, and 8, therefore no other cell in that column can have that value.")

    def test_naked_box(self):
        golden_coordinates = ['A4', 'A5', 'A6', 'B4', 'C5', 'C6']
        for c in self.board:
            if c.x == 2 and c.y == 3:
                c.candidates = [2, 8]
            if c.x == 1 and c.y == 4:
                c.candidates = [2, 5]
            if c.x == 1 and c.y == 5:
                c.candidates = [2, 5, 8]
        update = self.rule.find_update(self.board)
        for e in update.eliminations:
            self.assertTrue(str(e) in golden_coordinates)
            self.assertEqual(e.candidates, [2, 5, 8])
        self.assertEqual(update.rule_name, "Naked Triples")
        self.assertEqual(update.explanation, "Three cells B5, B6, and C4 have the same three candidates 2, 5, and 8, therefore no other cell in that box can have that value.")
