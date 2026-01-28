import unittest
from core.rules.chute_remote_pairs import ChuteRemotePairs
from core.board import Board

class TestChuteRemotePairs(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.rule = ChuteRemotePairs()

    def test_horizontal_chute(self):
        golden_coordinates = ['A1', 'B1', 'C1', 'G3', 'H3', 'I3']
        for c in self.board:
            if str(c) in ["C3", "G1"]:
                c.candidates = [4, 7]
            if str(c) in ["D2", "E2", "F2"]:
                c.candidates = [1,2,3,4]  # missing 7
        update = self.rule.find_update(self.board)
        for e in update.eliminations:
            self.assertTrue(str(e) in golden_coordinates)
            self.assertEqual(e.candidates, [4])
        self.assertEqual(update.rule_name, "Chute Remote Pairs")
        self.assertEqual(update.explanation, "Matching pairs 4 and 7 in cells C3 and G1 form a chute D2, E2, and F2 which doesn't contain 7. Therefore, C3 and G1 can't both be 7. Any 4 in cells A1, B1, C1, G3, H3, and I3 would force this. Therefore, 4 can't be in cells A1, B1, C1, G3, H3, and I3.")

    def test_vertical_chute(self):
        golden_coordinates = ['A1', 'A2', 'A3', 'C7', 'C8', 'C9']
        for c in self.board:
            if str(c) in ["C3", "A8"]:
                c.candidates = [4, 7]
            if str(c) in ["B4", "B5", "B6"]:
                c.candidates = [1,2,3,7]  # missing 4
        update = self.rule.find_update(self.board)
        for e in update.eliminations:
            self.assertTrue(str(e) in golden_coordinates)
            self.assertEqual(e.candidates, [7])
        self.assertEqual(update.rule_name, "Chute Remote Pairs")
        self.assertEqual(update.explanation, "Matching pairs 4 and 7 in cells A8 and C3 form a chute B4, B5, and B6 which doesn't contain 4. Therefore, A8 and C3 can't both be 4. Any 7 in cells A1, A2, A3, C7, C8, and C9 would force this. Therefore, 7 can't be in cells A1, A2, A3, C7, C8, and C9.")
