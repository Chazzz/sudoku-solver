import unittest
from core.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_blank_init(self):
        n = sum([len(c.candidates) for c in self.board])
        self.assertEqual(n, 729)  # 9^3
    
    def test_load_json_cells(self):
        golden_coordinates = ['A2', 'B2']
        s = "{\"cells\": [{\"x\": 1, \"y\": 1, \"candidates\": [2, 3]}, {\"x\": 0, \"y\": 1, \"candidates\": [2, 3]}]}"
        self.board.load_json(s)
        n = sum([len(c.candidates) for c in self.board])
        self.assertEqual(n, 715)
        for c in self.board:
            if str(c) in golden_coordinates:
                self.assertEqual(c.candidates, [2, 3])
    
    def test_load_json_cages(self):
        s = "{\"cages\": [{\"coordinates\": [{\"x\": 0, \"y\": 0}, {\"x\": 0, \"y\": 1}], \"sum\": 3}, {\"coordinates\": [{\"x\": 1, \"y\": 0}, {\"x\": 1, \"y\": 1}], \"sum\": 18}]}"
        self.board.load_json(s)
        self.assertEqual(len(self.board.cages), 2)
