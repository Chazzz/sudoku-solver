import unittest
from core.rules.captured_candidates import CapturedCandidates
from core.board import Board

class TestCapturedCandidates(unittest.TestCase):

    row_eight_cage = """
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
            "sum": 8
            }
        ]
        }"""

    col_eight_cage = """
        {
        "cages": [
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
            "sum": 8
            }
        ]
        }"""

    box_twenty_two_cage = """
        {
        "cages": [
            {
            "coordinates": [
                {
                "x": 3,
                "y": 4
                },
                {
                "x": 4,
                "y": 4
                },
                {
                "x": 4,
                "y": 5
                }
            ],
            "sum": 22
            }
        ]
        }"""
    
    bent_eight_cage = """
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
            "sum": 8
            }
        ]
        }"""

    def setUp(self):
        self.board = Board()
        self.rule = CapturedCandidates()

    def test_row(self):
        self.board.load_json(self.row_eight_cage)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 6)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['A1', 'B1', 'F1', 'G1', 'H1', 'I1'])
            self.assertEqual(e.candidates, [1])
        self.assertEqual(update.rule_name, "Killer Captured Candidates")
        self.assertEqual(update.explanation, "Given cage ['C1', 'D1', 'E1'] with sum 8, all valid combinations place 1 in C1, D1, and E1. Therefore, all other cells in the same row can't have that value.")

    def test_col(self):
        self.board.load_json(self.col_eight_cage)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 6)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['C1', 'C2', 'C6', 'C7', 'C8', 'C9'])
            self.assertEqual(e.candidates, [1])
        self.assertEqual(update.rule_name, "Killer Captured Candidates")
        self.assertEqual(update.explanation, "Given cage ['C3', 'C4', 'C5'] with sum 8, all valid combinations place 1 in C3, C4, and C5. Therefore, all other cells in the same column can't have that value.")

    def test_box(self):
        self.board.load_json(self.box_twenty_two_cage)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 6)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['D4', 'D6', 'E4', 'F4', 'F5', 'F6'])
            self.assertEqual(e.candidates, [9])
        self.assertEqual(update.rule_name, "Killer Captured Candidates")
        self.assertEqual(update.explanation, "Given cage ['D5', 'E5', 'E6'] with sum 22, all valid combinations place 9 in D5, E5, and E6. Therefore, all other cells in the same box can't have that value.")

    def test_completed_box(self):
        self.board.load_json(self.box_twenty_two_cage)
        for c in self.board:
            if c.x == 3 and c.y == 4:
                c.candidates = [9]
            if c.x == 4 and c.y == 4:
                c.candidates = [8]
            if c.x == 4 and c.y == 5:
                c.candidates = [5]
        update = self.rule.find_update(self.board)
        self.assertIsNone(update.eliminations)
    
    def test_bent_cage_row(self):
        self.board.load_json(self.bent_eight_cage)
        for c in self.board:
            if c.x == 2 and c.y == 0:
                c.candidates = [1, 2, 3, 4, 5]
            if c.x == 3 and c.y == 0:
                c.candidates = [1, 2, 3, 4, 5]
            if c.x == 2 and c.y == 1:
                c.candidates = [2, 3, 4, 5]    # 1 only in row 0 
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 7)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['A1', 'B1', 'E1', 'F1', 'G1', 'H1', 'I1'])
            self.assertEqual(e.candidates, [1])
        self.assertEqual(update.rule_name, "Killer Captured Candidates")
        self.assertEqual(update.explanation, "Given cage ['C1', 'D1', 'C2'] with sum 8, all valid combinations place 1 in C1 and D1. Therefore, all other cells in the same row can't have that value.")

    def test_bent_cage_col(self):
        self.board.load_json(self.bent_eight_cage)
        # Remove 1 from box first (test case applies to both)
        for c in self.board:
            if c.x // 3 == 0 and c.y // 3 == 0:
                c.candidates = list(range(2,10))
        for c in self.board:
            if c.x == 2 and c.y == 0:
                c.candidates = [1, 2, 3, 4, 5]
            if c.x == 3 and c.y == 0:
                c.candidates = [2, 3, 4, 5]  # 1 only in col 3
            if c.x == 2 and c.y == 1:
                c.candidates = [1, 2, 3, 4, 5] 
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 6)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['C4', 'C5', 'C6', 'C7', 'C8', 'C9'])
            self.assertEqual(e.candidates, [1])
        self.assertEqual(update.rule_name, "Killer Captured Candidates")
        self.assertEqual(update.explanation, "Given cage ['C1', 'D1', 'C2'] with sum 8, all valid combinations place 1 in C1 and C2. Therefore, all other cells in the same column can't have that value.")

    def test_bent_cage_box(self):
        self.board.load_json(self.bent_eight_cage)
        # Remove 1 from col first (test case applies to both)
        for c in self.board:
            if c.x == 2:
                c.candidates = list(range(2,10))
        for c in self.board:
            if c.x == 2 and c.y == 0:
                c.candidates = [1, 2, 3, 4, 5]
            if c.x == 3 and c.y == 0:
                c.candidates = [2, 3, 4, 5]  # 1 only in box (0, 0)
            if c.x == 2 and c.y == 1:
                c.candidates = [1, 2, 3, 4, 5] 
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 6)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['A1', 'A2', 'A3', 'B1', 'B2', 'B3'])
            self.assertEqual(e.candidates, [1])
        self.assertEqual(update.rule_name, "Killer Captured Candidates")
        self.assertEqual(update.explanation, "Given cage ['C1', 'D1', 'C2'] with sum 8, all valid combinations place 1 in C1 and C2. Therefore, all other cells in the same box can't have that value.")