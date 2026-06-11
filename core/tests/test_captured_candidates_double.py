import unittest
from core.rules.captured_candidates_double import CapturedCandidatesDouble
from core.board import Board

class TestCapturedCandidates(unittest.TestCase):
    row_eight_cage_double = """
        {
        "cages": [
            {
            "coordinates": [
                {
                "x": 2,
                "y": 2
                },
                {
                "x": 3,
                "y": 2
                },
                {
                "x": 2,
                "y": 3
                }
            ],
            "sum": 8
            },
            {
            "coordinates": [
                {
                "x": 5,
                "y": 2
                },
                {
                "x": 6,
                "y": 2
                },
                {
                "x": 6,
                "y": 3
                }
            ],
            "sum": 8
            }
        ],
        "cells": []
        }"""

    col_eight_cage_double = """
        {
        "cages": [
            {
            "coordinates": [
                {
                "x": 2,
                "y": 2
                },
                {
                "x": 3,
                "y": 2
                },
                {
                "x": 2,
                "y": 3
                }
            ],
            "sum": 8
            },
            {
            "coordinates": [
                {
                "x": 2,
                "y": 5
                },
                {
                "x": 2,
                "y": 6
                },
                {
                "x": 3,
                "y": 6
                }
            ],
            "sum": 8
            }
        ],
        "cells": []
        }"""

    box_twenty_two_cage_double = """
        {
        "cages": [
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
                "x": 0,
                "y": 3
                }
            ],
            "sum": 22
            },
            {
            "coordinates": [
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
                }
            ],
            "sum": 22
            }
        ],
        "cells": []
        }"""
    
    bent_eight_cage_double = """
        {
        "cages": [
            {
            "coordinates": [
                {
                "x": 2,
                "y": 2
                },
                {
                "x": 3,
                "y": 2
                },
                {
                "x": 2,
                "y": 3
                }
            ],
            "sum": 8
            },
            {
            "coordinates": [
                {
                "x": 5,
                "y": 1
                },
                {
                "x": 5,
                "y": 2
                },
                {
                "x": 5,
                "y": 3
                }
            ],
            "sum": 8
            }
        ],
        "cells": []
        }"""

    def setUp(self):
        self.board = Board()
        self.rule = CapturedCandidatesDouble()
        self.maxDiff = None

    def test_row_double(self):
        self.board.load_json(self.row_eight_cage_double)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 12)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['A3', 'B3', 'E3', 'H3', 'I3', 'A4', 'B4', 'D4', 'E4', 'F4', 'H4', 'I4'])
            self.assertEqual(e.candidates, [1])
        self.assertEqual(update.rule_name, "Killer Captured Candidates (Double)")
        self.assertEqual(update.explanation, "Given cage ['C3', 'D3', 'C4'] with sum 8 and cage ['F3', 'G3', 'G4'] with sum 8, all valid combinations place 1 in C3, C4, D3, F3, G3, and G4. Therefore, all other cells in the same rows can't have that value.")

    def test_col_double(self):
        self.board.load_json(self.col_eight_cage_double)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 12)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['C1', 'C2', 'C5', 'C8', 'C9', 'D1', 'D2', 'D4', 'D5', 'D6', 'D8', 'D9'])
            self.assertEqual(e.candidates, [1])
        self.assertEqual(update.rule_name, "Killer Captured Candidates (Double)")
        self.assertEqual(update.explanation, "Given cage ['C3', 'D3', 'C4'] with sum 8 and cage ['C6', 'C7', 'D7'] with sum 8, all valid combinations place 1 in C3, C4, D3, C6, C7, and D7. Therefore, all other cells in the same columns can't have that value.")

    def test_box_double(self):
        self.board.load_json(self.box_twenty_two_cage_double)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 12)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['A5', 'A6', 'B4', 'B5', 'B6', 'C6', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2'])
            self.assertEqual(e.candidates, [9])
        self.assertEqual(update.rule_name, "Killer Captured Candidates (Double)")
        self.assertEqual(update.explanation, "Given cage ['A3', 'B3', 'A4'] with sum 22 and cage ['C3', 'C4', 'C5'] with sum 22, all valid combinations place 9 in A3, A4, B3, C3, C4, and C5. Therefore, all other cells in the same boxes can't have that value.")

    def test_completed_box_double(self):
        self.board.load_json(self.box_twenty_two_cage_double)
        for c in self.board:
            if c.x == 0 and c.y == 2:
                c.candidates = [9]
            if c.x == 1 and c.y == 2:
                c.candidates = [8]
            if c.x == 0 and c.y == 3:
                c.candidates = [5]
            if c.x == 2 and c.y == 2:
                c.candidates = [9]
            if c.x == 2 and c.y == 3:
                c.candidates = [8]
            if c.x == 2 and c.y == 4:
                c.candidates = [5]
        update = self.rule.find_update(self.board)
        self.assertIsNone(update.eliminations)
    
    def test_bent_cage_row_double(self):
        self.board.load_json(self.bent_eight_cage_double)
        for c in self.board:
            # 1 only in row 3/4
            if c.x == 5 and c.y == 1:
                c.candidates = [2, 3, 4, 5]     
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 13)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['A3', 'B3', 'E3', 'G3', 'H3', 'I3', 'A4', 'B4', 'D4', 'E4', 'G4', 'H4', 'I4'])
            self.assertEqual(e.candidates, [1])
        self.assertEqual(update.rule_name, "Killer Captured Candidates (Double)")
        self.assertEqual(update.explanation, "Given cage ['C3', 'D3', 'C4'] with sum 8 and cage ['F2', 'F3', 'F4'] with sum 8, all valid combinations place 1 in C3, C4, D3, F3, and F4. Therefore, all other cells in the same rows can't have that value.")
