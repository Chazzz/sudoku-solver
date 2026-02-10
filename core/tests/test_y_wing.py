import unittest
from core.rules.y_wing import YWing
from core.board import Board

class TestYWing(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.rule = YWing()

    def test_ywing_naked_triple(self):
        for c in self.board:
            if str(c) == "A1":
                c.candidates = [1, 2]
            if str(c) == "B1":
                c.candidates = [2, 3]
            if str(c) == "D1":
                c.candidates = [1, 3]
        update = self.rule.find_update(self.board)
        # print([str(e) for e in update.eliminations])
        self.assertEqual(len(update.eliminations), 6)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['C1', 'E1', 'F1', 'G1', 'H1', 'I1'])
            self.assertEqual(e.candidates, [3])
        self.assertEqual(update.rule_name, "Y Wing")
        self.assertEqual(update.explanation, "Double at A1 forms two wings with D1 and B1, eliminating all candidates 3 that can see both D1 and B1.")

    def test_ywing_5_corrections(self):
        for c in self.board:
            if str(c) == "A1":
                c.candidates = [1, 2]
            if str(c) == "B1":
                c.candidates = [2, 3]
            if str(c) == "A4":
                c.candidates = [1, 3]
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 5)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['A2', 'A3', 'B4', 'B5', 'B6'])
            self.assertEqual(e.candidates, [3])
        self.assertEqual(update.rule_name, "Y Wing")
        self.assertEqual(update.explanation, "Double at A1 forms two wings with A4 and B1, eliminating all candidates 3 that can see both A4 and B1.")


    def test_ywing_1_correction(self):
        for c in self.board:
            if str(c) == "A1":
                c.candidates = [1, 2]
            if str(c) == "D1":
                c.candidates = [2, 3]
            if str(c) == "A4":
                c.candidates = [1, 3]
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1)
        for e in update.eliminations:
            self.assertTrue(str(e) in ['D4'])
            self.assertEqual(e.candidates, [3])
        self.assertEqual(update.rule_name, "Y Wing")
        self.assertEqual(update.explanation, "Double at A1 forms two wings with A4 and D1, eliminating all candidates 3 that can see both A4 and D1.")