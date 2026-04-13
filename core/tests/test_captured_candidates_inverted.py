import unittest
from core.rules.captured_candidates_inverted import CapturedCandidatesInverted
from core.board import Board

class TestCapturedCandidatesInverted(unittest.TestCase):
    row_nine_cage = """
        {
        "cages": [
            {
            "coordinates": [
                {
                "x": 2,
                "y": 0
                },
                {
                "x": 3,
                "y": 0
                },
                {
                "x": 4,
                "y": 0
                }
            ],
            "sum": 9
            }
        ],
        "cells": []
        }"""

    col_nine_cage = """
        {
        "cages": [
            {
            "coordinates": [
                {
                "x": 0,
                "y": 2
                },
                {
                "x": 0,
                "y": 3
                },
                {
                "x": 0,
                "y": 4
                }
            ],
            "sum": 9
            }
        ],
        "cells": []
        }"""

    bent_nine_cage = """
        {
        "cages": [
            {
            "coordinates": [
                {
                "x": 2,
                "y": 0
                },
                {
                "x": 3,
                "y": 0
                },
                {
                "x": 2,
                "y": 1
                }
            ],
            "sum": 9
            }
        ],
        "cells": []
        }"""
    
    bent_twelve_cage = """
        {
        "cages": [
            {
            "coordinates": [
                {
                "x": 2,
                "y": 0
                },
                {
                "x": 3,
                "y": 0
                },
                {
                "x": 4,
                "y": 0
                },
                {
                "x": 2,
                "y": 1
                }
            ],
            "sum": 12
            }
        ],
        "cells": []
        }"""

    def setUp(self):
        self.board = Board()
        self.rule = CapturedCandidatesInverted()

    def test_row(self):
        self.board.load_json(self.row_nine_cage)
        for c in self.board:
            if c.y == 0:
                if c.x not in [2, 3, 4]:
                    c.candidates = list(range(2,10))  # Capture the 1 in row
                else:
                    c.candidates = list(range(1,7))  # Eliminate easy combos
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 3)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['C1', 'D1', 'E1'])
            self.assertEqual(e.candidates, [4])
        self.assertEqual(update.rule_name, "Killer Captured Candidates 2")
        self.assertEqual(update.explanation, "Given 1 is only possible in C1, D1, and E1 for all cells in that row, 1 must be in cage ['C1', 'D1', 'E1'] with sum 9. With that requirement, the following values are never used to form a valid sum in cage ['C1', 'D1', 'E1'] with sum 9: 4 at C1, 4 at D1, and 4 at E1.")

    def test_col(self):
        self.board.load_json(self.col_nine_cage)
        for c in self.board:
            if c.x == 0:
                if c.y not in [2, 3, 4]:
                    c.candidates = list(range(2,10))  # Capture the 1 in row
                else:
                    c.candidates = list(range(1,7))  # Eliminate easy combos
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 3)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['A3', 'A4', 'A5'])
            self.assertEqual(e.candidates, [4])
        self.assertEqual(update.rule_name, "Killer Captured Candidates 2")
        self.assertEqual(update.explanation, "Given 1 is only possible in A3, A4, and A5 for all cells in that column, 1 must be in cage ['A3', 'A4', 'A5'] with sum 9. With that requirement, the following values are never used to form a valid sum in cage ['A3', 'A4', 'A5'] with sum 9: 4 at A3, 4 at A4, and 4 at A5.")

    def test_box(self):
        self.board.load_json(self.bent_nine_cage)
        for c in self.board:
            if c.x // 3 == 0 and c.y // 3 == 0:
                c.candidates = list(range(2,10))  # Capture the 1 in box
            if (c.x, c.y) in [(2,0), (2,1), (3, 0)]:
                c.candidates = list(range(1,7))  # Eliminate easy combos
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 3)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['C1', 'C2', 'D1'])
            if str(e) in ['C1', 'C2']:
                self.assertEqual(e.candidates, [4])
            if str(e) in ['D1']:
                self.assertEqual(e.candidates, [1,4])
        self.assertEqual(update.rule_name, "Killer Captured Candidates 2")
        self.assertEqual(update.explanation, "Given 1 is only possible in C1 and C2 for all cells in that box, 1 must be in cage ['C1', 'D1', 'C2'] with sum 9. With that requirement, the following values are never used to form a valid sum in cage ['C1', 'D1', 'C2'] with sum 9: 4 at C1, 4 at C2, 1 at D1, and 4 at D1.")

    def test_bent_col(self):
        self.board.load_json(self.bent_nine_cage)
        for c in self.board:
            if c.x == 2:
                c.candidates = list(range(2,10))  # Capture the 1 in col
            if (c.x, c.y) in [(2,0), (2,1), (3, 0)]:
                c.candidates = list(range(1,7))  # Eliminate easy combos
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 3)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['C1', 'C2', 'D1'])
            if str(e) in ['C1', 'C2']:
                self.assertEqual(e.candidates, [4])
            if str(e) in ['D1']:
                self.assertEqual(e.candidates, [1,4])
        self.assertEqual(update.rule_name, "Killer Captured Candidates 2")
        self.assertEqual(update.explanation, "Given 1 is only possible in C1 and C2 for all cells in that column, 1 must be in cage ['C1', 'D1', 'C2'] with sum 9. With that requirement, the following values are never used to form a valid sum in cage ['C1', 'D1', 'C2'] with sum 9: 4 at C1, 4 at C2, 1 at D1, and 4 at D1.")

    def test_multiple_captured(self):
        self.board.load_json(self.bent_twelve_cage)
        # Remove 1 from col first (test case applies to both)
        for c in self.board:
            if c.y == 0:
                c.candidates = [1, 2, 4, 5, 7, 8, 9]  # capture 3, 6
        for c in self.board:
            if (c.x, c.y) in [(2,0), (2,1), (3, 0), (4, 0)]:
                c.candidates = list(range(1,7))  # Eliminate easy combos
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 4)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['C1', 'C2', 'D1', 'E1'])
            if str(e) in ['C1', 'D1', 'E1']:
                self.assertEqual(e.candidates, [4, 5])
            if str(e) in ['C2']:
                self.assertEqual(e.candidates, [3, 4, 5, 6])
        self.assertEqual(update.rule_name, "Killer Captured Candidates 2")
        self.assertEqual(update.explanation, "Given 3 and 6 are only possible in C1, D1, and E1 for all cells in that row, 3 and 6 must be in cage ['C1', 'D1', 'E1', 'C2'] with sum 12. With that requirement, the following values are never used to form a valid sum in cage ['C1', 'D1', 'E1', 'C2'] with sum 12: 4 at C1, 5 at C1, 3 at C2, 4 at C2, 5 at C2, 6 at C2, 4 at D1, 5 at D1, 4 at E1, and 5 at E1.")

    