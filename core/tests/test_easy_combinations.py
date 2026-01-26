import unittest
from core.rules.easy_combinations import EasyCombinations
from core.board import Board

class TestEasyCombinations(unittest.TestCase):

    one_three_cage = """
        {
        "cages": [
            {
            "coordinates": [
                {
                "x": 0,
                "y": 0
                },
                {
                "x": 1,
                "y": 0
                }
            ],
            "sum": 3
            }
        ]
        }"""
    
    big_twenty_cage = """
        {
        "cages": [
            {
            "coordinates": [
                {
                "x": 0,
                "y": 0
                },
                {
                "x": 1,
                "y": 0
                },
                {
                "x": 2,
                "y": 0
                }
            ],
            "sum": 13
            },
            {
            "coordinates": [
                {
                "x": 0,
                "y": 1
                },
                {
                "x": 1,
                "y": 1
                },
                {
                "x": 2,
                "y": 1
                }
            ],
            "sum": 20
            },
            {
            "coordinates": [
                {
                "x": 0,
                "y": 2
                },
                {
                "x": 1,
                "y": 2
                },
                {
                "x": 2,
                "y": 2
                }
            ],
            "sum": 12
            }
        ]
        }"""

    def setUp(self):
        self.board = Board()
        self.rule = EasyCombinations()

    def test_basic_case(self):
        self.board.load_json(self.one_three_cage)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 2) 
        for e in update.eliminations:
            self.assertTrue(str(e) in ["A1", "B1"])
            self.assertEqual(e.candidates, [3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Easy Combinations")
        self.assertEqual(update.explanation, "Cage ['A1', 'B1'] with sum 3 can only be completed using values 1 and 2.")

    def test_big_case(self):
        self.board.load_json(self.big_twenty_cage)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 3)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['A2', 'B2', 'C2'])
            self.assertEqual(e.candidates, [1, 2])
        self.assertEqual(update.rule_name, "Killer Easy Combinations")
        self.assertEqual(update.explanation, "Cage ['A2', 'B2', 'C2'] with sum 20 can only be completed using values 3, 4, 5, 6, 7, 8, and 9.")

    def test_big_case_with_single(self):
        self.board.load_json(self.big_twenty_cage)
        for c in self.board:
            if c.x in [0, 2] and c.y == 1:
                c.candidates = range(4,10)
            if c.x == 1 and c.y == 1:
                c.candidates = [3]
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 2)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['A2', 'C2'])
            self.assertEqual(e.candidates, [4, 5, 6, 7])
        self.assertEqual(update.rule_name, "Killer Easy Combinations")
        self.assertEqual(update.explanation, "Cage ['A2', 'B2', 'C2'] with sum 20 with values [3] at ['B2'] can only be completed using values 8 and 9.")

    def test_basic_case_filled_in(self):
        self.board.load_json(self.one_three_cage)
        for c in self.board:
            if c.x == 0 and c.y == 0:
                c.candidates = [1]
            if c.x == 1 and c.y == 0:
                c.candidates = [2]
        update = self.rule.find_update(self.board)
        self.assertIsNone(update.eliminations)