import unittest
from core.rules.pointing_lines import PointingLines
from core.board import Board

class TestPointingLines(unittest.TestCase):
    row_one_value_one_box_three = """
        {
        "cages": [
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
                },
                {
                "x": 3,
                "y": 1
                },
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
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
            ]
            },
            {
            "x": 1,
            "y": 2,
            "candidates": [
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
            ]
            },
            {
            "x": 2,
            "y": 2,
            "candidates": [
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
            ]
            }
        ]
        }"""

    row_one_value_nine_box_three = """
        {
        "cages": [
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
                },
                {
                "x": 3,
                "y": 1
                },
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
            "x": 2,
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

    row_nine_value_one_box_one = """
        {
        "cages": [
            {
            "coordinates": [
                {
                "x": 3,
                "y": 6
                },
                {
                "x": 4,
                "y": 6
                },
                {
                "x": 5,
                "y": 6
                },
                {
                "x": 6,
                "y": 6
                },
                {
                "x": 6,
                "y": 7
                },
                {
                "x": 7,
                "y": 7
                },
                {
                "x": 8,
                "y": 7
                }
            ],
            "sum": 36
            }
        ],
        "cells": [
            {
            "x": 3,
            "y": 7,
            "candidates": [
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
            ]
            },
            {
            "x": 4,
            "y": 7,
            "candidates": [
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
            ]
            },
            {
            "x": 5,
            "y": 7,
            "candidates": [
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
            ]
            }
        ]
        }"""

    col_one_value_one_box_three = """{
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
            "x": 1,
            "y": 3,
            "candidates": [
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
            ]
            },
            {
            "x": 1,
            "y": 4,
            "candidates": [
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
            ]
            },
            {
            "x": 1,
            "y": 5,
            "candidates": [
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
            ]
            }
        ]
        }"""

    def setUp(self):
        self.board = Board()
        self.rule = PointingLines()

    def test_pointing_row(self):
        self.board.load_json(self.row_one_value_one_box_three)
        update = self.rule.find_update(self.board)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['G1', 'H1', 'I1'])
            self.assertEqual(e.candidates, [1])
        self.assertEqual(update.rule_name, "Pointing Lines")
        self.assertEqual(update.explanation, "For row 1, 1 must be in box (0, 0) or box (1, 0), because 1 cannot be placed both in box (0, 0) and box (1, 0) without using row 1.")

    def test_pointing_row_value_nine(self):
        self.board.load_json(self.row_one_value_nine_box_three)
        update = self.rule.find_update(self.board)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['G1', 'H1', 'I1'])
            self.assertEqual(e.candidates, [9])
        self.assertEqual(update.rule_name, "Pointing Lines")
        self.assertEqual(update.explanation, "For row 1, 9 must be in box (0, 0) or box (1, 0), because 9 cannot be placed both in box (0, 0) and box (1, 0) without using row 1.")

    def test_pointing_row_nine(self):
        self.board.load_json(self.row_nine_value_one_box_one)
        update = self.rule.find_update(self.board)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['A9', 'B9', 'C9'])
            self.assertEqual(e.candidates, [1])
        self.assertEqual(update.rule_name, "Pointing Lines")
        self.assertEqual(update.explanation, "For row 9, 1 must be in box (1, 2) or box (2, 2), because 1 cannot be placed both in box (1, 2) and box (2, 2) without using row 9.")

    def test_pointing_col(self):
        self.board.load_json(self.col_one_value_one_box_three)
        update = self.rule.find_update(self.board)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['A7', 'A8', 'A9'])
            self.assertEqual(e.candidates, [1])
        self.assertEqual(update.rule_name, "Pointing Lines")
        self.assertEqual(update.explanation, "For column A, 1 must be in box (0, 0) or box (0, 1), because 1 cannot be placed both in box (0, 0) and box (0, 1) without using column A.")
