import unittest
from core.rules.generalized_captured_candidates import GeneralizedCapturedCandidates
from core.board import Board

class TestGeneralizedCapturedCandidates(unittest.TestCase):

    cage_captured = """
        {
        "cages": [
            {
            "coordinates": [
                {
                "x": 1,
                "y": 0
                },
                {
                "x": 1,
                "y": 1
                },
                {
                "x": 1,
                "y": 2
                },
                {
                "x": 2,
                "y": 2
                },
                {
                "x": 2,
                "y": 3
                },
                {
                "x": 2,
                "y": 4
                },
                {
                "x": 2,
                "y": 5
                }
            ],
            "sum": 36
            }
        ],
        "cells": []
        }"""

    box_captured = """
        {
        "cages": [
            {
            "coordinates": [
                {
                "x": 1,
                "y": 0
                },
                {
                "x": 1,
                "y": 1
                },
                {
                "x": 1,
                "y": 2
                },
                {
                "x": 2,
                "y": 2
                },
                {
                "x": 2,
                "y": 3
                },
                {
                "x": 2,
                "y": 4
                },
                {
                "x": 2,
                "y": 5
                }
            ],
            "sum": 36
            }
        ],
        "cells": [
            {
            "x": 0,
            "y": 0,
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
            "y": 0,
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
            },
            {
            "x": 0,
            "y": 2,
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

    row_captured = """
        {
        "cages": [
            {
            "coordinates": [
                {
                "x": 2,
                "y": 0
                },
                {
                "x": 2,
                "y": 1
                },
                {
                "x": 2,
                "y": 2
                },
                {
                "x": 3,
                "y": 2
                },
                {
                "x": 3,
                "y": 3
                },
                {
                "x": 3,
                "y": 4
                },
                {
                "x": 3,
                "y": 5
                }
            ],
            "sum": 36
            }
        ],
        "cells": [
            {
            "x": 0,
            "y": 2,
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
            "y": 2,
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
            "x": 4,
            "y": 2,
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
            "x": 5,
            "y": 2,
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
            "x": 6,
            "y": 2,
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
            "x": 7,
            "y": 2,
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
            "x": 8,
            "y": 2,
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

    col_captured = """
        {
        "cages": [
            {
            "coordinates": [
                {
                "x": 3,
                "y": 2
                },
                {
                "x": 4,
                "y": 2
                },
                {
                "x": 5,
                "y": 2
                },
                {
                "x": 0,
                "y": 3
                },
                {
                "x": 1,
                "y": 3
                },
                {
                "x": 2,
                "y": 3
                },
                {
                "x": 3,
                "y": 3
                }
            ],
            "sum": 36
            }
        ],
        "cells": [
            {
            "x": 3,
            "y": 0,
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
            "x": 3,
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
            "x": 3,
            "y": 4,
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
            "x": 3,
            "y": 5,
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
            "x": 3,
            "y": 6,
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
            "x": 3,
            "y": 7,
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
            "x": 3,
            "y": 8,
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

    def setUp(self):
        self.board = Board()
        self.rule = GeneralizedCapturedCandidates()

    def test_cage(self):
        self.board.load_json(self.cage_captured)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 2)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['C1', 'C2'])
            self.assertEqual(e.candidates, [9])
        self.assertEqual(update.rule_name, "Generalized Captured Candidates")
        self.assertEqual(update.explanation, "Given cage ['B1', 'B2', 'B3', 'C3', 'C4', 'C5', 'C6'] with sum 36, all valid combinations place 9 in B1, B2, B3, C3, C4, C5, and C6. Therefore, all other cells which can see B1, B2, B3, C3, C4, C5, and C6 can't have that value.")

    def test_box(self):
        self.board.load_json(self.box_captured)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 3)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['C4', 'C5', 'C6'])
            self.assertEqual(e.candidates, [9])
        self.assertEqual(update.rule_name, "Generalized Captured Candidates")
        self.assertEqual(update.explanation, "Given box (0, 0), all valid combinations place 9 in B1, B2, B3, and C3. Therefore, all other cells which can see B1, B2, B3, and C3 can't have that value.")

    def test_row(self):
        self.board.load_json(self.row_captured)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 5)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['C1', 'C2', 'D4', 'D5', 'D6'])
            self.assertEqual(e.candidates, [9])
        self.assertEqual(update.rule_name, "Generalized Captured Candidates")
        self.assertEqual(update.explanation, "Given row 3, all valid combinations place 9 in C3 and D3. Therefore, all other cells which can see C3 and D3 can't have that value.")

    def test_col(self):
        self.board.load_json(self.col_captured)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 5)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['A4', 'B4', 'C4', 'E3', 'F3'])
            self.assertEqual(e.candidates, [9])
        self.assertEqual(update.rule_name, "Generalized Captured Candidates")
        self.assertEqual(update.explanation, "Given col D, all valid combinations place 9 in D3 and D4. Therefore, all other cells which can see D3 and D4 can't have that value.")


