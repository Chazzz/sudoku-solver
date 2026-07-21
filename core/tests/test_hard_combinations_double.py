import unittest
from core.rules.hard_combinations_double import HardCombinationsDouble
from core.board import Board

class TestHardCombinationsDouble(unittest.TestCase):

    basic_double_case = """
        {
        "cages": [
            {
            "coordinates": [
                {
                "x": 1,
                "y": 0
                },
                {
                "x": 2,
                "y": 0
                },
                {
                "x": 2,
                "y": 1
                }
            ],
            "sum": 11
            },
            {
            "coordinates": [
                {
                "x": 3,
                "y": 0
                },
                {
                "x": 4,
                "y": 0
                },
                {
                "x": 3,
                "y": 1
                }
            ],
            "sum": 15
            }
        ],
        "cells": [
            {
            "x": 1,
            "y": 0,
            "candidates": [
                1,
                2,
                3
            ]
            },
            {
            "x": 2,
            "y": 0,
            "candidates": [
                1,
                2,
                3
            ]
            },
            {
            "x": 3,
            "y": 0,
            "candidates": [
                1,
                2,
                9
            ]
            },
            {
            "x": 4,
            "y": 0,
            "candidates": [
                1,
                2,
                9
            ]
            },
            {
            "x": 2,
            "y": 1,
            "candidates": [
                6,
                7,
                8
            ]
            },
            {
            "x": 3,
            "y": 1,
            "candidates": [
                4,
                5
            ]
            }
        ]
        }"""

    null_double_case_with_eight = """
        {
        "cages": [
            {
            "coordinates": [
                {
                "x": 1,
                "y": 0
                },
                {
                "x": 2,
                "y": 0
                },
                {
                "x": 2,
                "y": 1
                }
            ],
            "sum": 11
            },
            {
            "coordinates": [
                {
                "x": 6,
                "y": 3
                },
                {
                "x": 7,
                "y": 3
                },
                {
                "x": 6,
                "y": 4
                }
            ],
            "sum": 15
            },
            {
            "coordinates": [
                {
                "x": 4,
                "y": 1
                },
                {
                "x": 5,
                "y": 1
                },
                {
                "x": 4,
                "y": 2
                }
            ],
            "sum": 12
            },
            {
            "coordinates": [
                {
                "x": 3,
                "y": 6
                },
                {
                "x": 3,
                "y": 7
                },
                {
                "x": 3,
                "y": 8
                }
            ],
            "sum": 8
            }
        ],
        "cells": [
            {
            "x": 1,
            "y": 0,
            "candidates": [
                1,
                2,
                3
            ]
            },
            {
            "x": 2,
            "y": 0,
            "candidates": [
                1,
                2,
                3
            ]
            },
            {
            "x": 2,
            "y": 1,
            "candidates": [
                6,
                7,
                8
            ]
            },
            {
            "x": 6,
            "y": 3,
            "candidates": [
                1,
                2,
                9
            ]
            },
            {
            "x": 7,
            "y": 3,
            "candidates": [
                1,
                2,
                9
            ]
            },
            {
            "x": 6,
            "y": 4,
            "candidates": [
                4,
                5
            ]
            }
        ]
        }"""

    def setUp(self):
        self.board = Board()
        self.rule = HardCombinationsDouble()

    def test_basic_case(self):
        self.board.load_json(self.basic_double_case)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertTrue(str(e) in ["C2"])
            self.assertEqual(e.candidates, [8])
        self.assertEqual(update.rule_name, "Double Killer Hard Combinations")
        self.assertEqual(update.explanation, "When comparing ['B1', 'C1', 'C2'] with sum 11 and ['D1', 'E1', 'D2'] with sum 15, the following value is never used to form a valid arrangement of the two cages: 8 at C2.")

    # only 2 cages that can see each other should be checked
    def test_optimization(self):
        self.board.load_json(self.null_double_case_with_eight)
        update = self.rule.find_update(self.board)
        self.assertIsNone(update.eliminations)