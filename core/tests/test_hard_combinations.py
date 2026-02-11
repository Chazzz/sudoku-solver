import unittest
from core.rules.hard_combinations import HardCombinations
from core.board import Board

class TestHardCombinations(unittest.TestCase):

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
        ],
        "cells": [
            {
            "x": 0,
            "y": 0,
            "candidates": [
                1
            ]
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
        ],
        "cells": [
            {
            "x": 0,
            "y": 1,
            "candidates": [
                3,
                4
            ]
            },
            {
            "x": 1,
            "y": 1,
            "candidates": [
                9
            ]
            }
        ]
        }"""

    hard_combination = """
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
            "sum": 15
            }
        ],
        "cells": [
            {
            "x": 0,
            "y": 0,
            "candidates": [
                1,
                4,
                7,
                9
            ]
            },
            {
            "x": 1,
            "y": 0,
            "candidates": [
                4,
                5,
                6,
                9
            ]
            },
            {
            "x": 2,
            "y": 0,
            "candidates": [
                1,
                2,
                5,
                7
            ]
            }
        ]
        }"""

    def setUp(self):
        self.board = Board()
        self.rule = HardCombinations()

    def test_basic_case(self):
        self.board.load_json(self.one_three_cage)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertTrue(str(e) in ["B1"])
            self.assertEqual(e.candidates, [1, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Hard Combinations")
        self.assertEqual(update.explanation, "The following values are never used to form a valid sum in cage ['A1', 'B1'] with sum 3: 1 at B1, 3 at B1, 4 at B1, 5 at B1, 6 at B1, 7 at B1, 8 at B1, and 9 at B1.")

    def test_big_case(self):
        self.board.load_json(self.big_twenty_cage)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['C2'])
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 6, 9])
        self.assertEqual(update.rule_name, "Killer Hard Combinations")
        self.assertEqual(update.explanation, "The following values are never used to form a valid sum in cage ['A2', 'B2', 'C2'] with sum 20: 1 at C2, 2 at C2, 3 at C2, 4 at C2, 5 at C2, 6 at C2, and 9 at C2.")

    def test_hard_combination(self):
        self.board.load_json(self.hard_combination)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['C1'])
            self.assertEqual(e.candidates, [7])
        self.assertEqual(update.rule_name, "Killer Hard Combinations")
        self.assertEqual(update.explanation, "The following values are never used to form a valid sum in cage ['A1', 'B1', 'C1'] with sum 15: 7 at C1.")

    # def test_big_case_with_single(self):
    #     self.board.load_json(self.big_twenty_cage)
    #     for c in self.board:
    #         if c.x in [0, 2] and c.y == 1:
    #             c.candidates = range(4,10)
    #         if c.x == 1 and c.y == 1:
    #             c.candidates = [3]
    #     update = self.rule.find_update(self.board)
    #     self.assertEqual(len(update.eliminations), 2)
    #     for e in update.eliminations:
    #         self.assertTrue(str(e) in ['A2', 'C2'])
    #         self.assertEqual(e.candidates, [4, 5, 6, 7])
    #     self.assertEqual(update.rule_name, "Killer Easy Combinations")
    #     self.assertEqual(update.explanation, "Cage ['A2', 'B2', 'C2'] with sum 20 with values [3] at ['B2'] can only be completed using values 8 and 9.")

    # def test_basic_case_filled_in(self):
    #     self.board.load_json(self.one_three_cage)
    #     for c in self.board:
    #         if c.x == 0 and c.y == 0:
    #             c.candidates = [1]
    #         if c.x == 1 and c.y == 0:
    #             c.candidates = [2]
    #     update = self.rule.find_update(self.board)
    #     self.assertIsNone(update.eliminations)