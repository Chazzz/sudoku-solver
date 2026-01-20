import unittest
from core.rules.naked_doubles import NakedDoubles
from core.board import Board

class TestNakedDoubles(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.rule = NakedDoubles()
    
    def test_basic_case(self):
        golden_coordinates = ['B1', 'C1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'B2', 'B3', 'C2', 'C3']
        s = "[{\"x\": 0, \"y\": 0, \"candidates\": [2, 3]}, {\"x\": 0, \"y\": 1, \"candidates\": [2, 3]}]"
        self.board.load_json(s)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 13*2)  # column and box (with 1 overlap removed)
        for e in update.eliminations:
            self.assertTrue(str(e) in golden_coordinates)
            self.assertTrue(e.candidates[0] in [2, 3])  # 13 of each
        self.assertEqual(update.rule_name, "Naked Doubles")
        self.assertEqual(update.explanation, "Given A1 and A2 can only be 2 and 3, no other cells in same row, column, or box can also be 2 or 3.")

    def test_row_only(self):
        golden_coordinates = ["B1", "C1", "E1", "F1", "G1", "H1", "I1"]
        s = "[{\"x\": 0, \"y\": 0, \"candidates\": [2, 3]}, {\"x\": 3, \"y\": 0, \"candidates\": [2, 3]}]"
        self.board.load_json(s)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 7*2)
        for e in update.eliminations:
            self.assertTrue(str(e) in golden_coordinates)
            self.assertTrue(e.candidates[0] in [2, 3])  # 13 of each
        self.assertEqual(update.rule_name, "Naked Doubles")
        self.assertEqual(update.explanation, "Given A1 and D1 can only be 2 and 3, no other cells in same row, column, or box can also be 2 or 3.")
    
    def test_box_only(self):
        golden_coordinates = ["A2", "A3", "B1", "B3", "C1", "C2", "C3"]
        s = "[{\"x\": 0, \"y\": 0, \"candidates\": [2, 3]}, {\"x\": 1, \"y\": 1, \"candidates\": [2, 3]}]"
        self.board.load_json(s)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 7*2)
        for e in update.eliminations:
            self.assertTrue(str(e) in golden_coordinates)
            self.assertTrue(e.candidates[0] in [2, 3])  # 13 of each
        self.assertEqual(update.rule_name, "Naked Doubles")
        self.assertEqual(update.explanation, "Given A1 and B2 can only be 2 and 3, no other cells in same row, column, or box can also be 2 or 3.")
    
    def test_col_only(self):
        golden_coordinates = ["A2", "A3", "A4", "A6", "A7", "A8", "A9"]
        s = "[{\"x\": 0, \"y\": 0, \"candidates\": [2, 3]}, {\"x\": 0, \"y\": 4, \"candidates\": [2, 3]}]"
        self.board.load_json(s)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 7*2)
        for e in update.eliminations:
            self.assertTrue(str(e) in golden_coordinates)
            self.assertTrue(e.candidates[0] in [2, 3])  # 13 of each
        self.assertEqual(update.rule_name, "Naked Doubles")
        self.assertEqual(update.explanation, "Given A1 and A5 can only be 2 and 3, no other cells in same row, column, or box can also be 2 or 3.")
    

