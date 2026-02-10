import unittest
from core.rules.medium_combinations import MediumCombinations
from core.board import Board

class TestMediumCombinations(unittest.TestCase):

    one_five_cage = """
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
            "sum": 5
            }
        ],
        "cells": [
            {
            "x": 0,
            "y": 0,
            "candidates": [
                2,
                3,
                4
            ]
            },
            {
            "x": 1,
            "y": 0,
            "candidates": [
                2,
                3,
                4
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
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8
            ]
            },
            {
            "x": 1,
            "y": 1,
            "candidates": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8
            ]
            },
            {
            "x": 2,
            "y": 1,
            "candidates": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8
            ]
            }
        ]
        }"""

    big_twenty_cage_set = """
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
                9
            ]
            },
            {
            "x": 1,
            "y": 1,
            "candidates": [
                4,
                5,
                6,
                7,
                8
            ]
            },
            {
            "x": 2,
            "y": 1,
            "candidates": [
                4,
                5,
                6,
                7,
                8
            ]
            }
        ]
        }"""

    def setUp(self):
        self.board = Board()
        self.rule = MediumCombinations()

    def test_basic_case(self):
        self.board.load_json(self.one_five_cage)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 2) 
        for e in update.eliminations:
            self.assertTrue(str(e) in ["A1", "B1"])
            self.assertEqual(e.candidates, [4])
        self.assertEqual(update.rule_name, "Killer Medium Combinations")
        self.assertEqual(update.explanation, "Cage ['A1', 'B1'] with sum 5 can only be completed using values 2 and 3.")

    def test_big_cage(self):
        self.board.load_json(self.big_twenty_cage)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 3)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['A2', 'B2', 'C2'])
            self.assertEqual(e.candidates, [1, 2, 3, 4, 6])
        self.assertEqual(update.rule_name, "Killer Medium Combinations")
        self.assertEqual(update.explanation, "Cage ['A2', 'B2', 'C2'] with sum 20 can only be completed using values 5, 7, and 8.")

    def test_big_cage_set(self):
        self.board.load_json(self.big_twenty_cage_set)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 2)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['B2', 'C2'])
            self.assertEqual(e.candidates, [8])
        self.assertEqual(update.rule_name, "Killer Medium Combinations")
        self.assertEqual(update.explanation, "Cage ['A2', 'B2', 'C2'] with sum 20 with values [9] at ['A2'] can only be completed using values 4, 5, 6, and 7.")