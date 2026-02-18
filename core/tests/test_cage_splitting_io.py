import unittest
from core.rules.cage_splitting_io import CageSplittingIO
from core.board import Board
from core.cage import Cage
from core.coordinates import Coordinates

# row/column/box
# splitting an inferred box yes/no


class TestCageSplittingIO(unittest.TestCase):
    one_row_with_6_innie = """
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
                "x": 5,
                "y": 0
                },
                {
                "x": 6,
                "y": 0
                }
            ],
            "sum": 39
            },
            {
            "coordinates": [
                {
                "x": 7,
                "y": 0
                },
                {
                "x": 8,
                "y": 0
                },
                {
                "x": 8,
                "y": 1
                },
                {
                "x": 8,
                "y": 2
                }
            ],
            "sum": 16
            }
        ],
        "cells": []
        }"""

    one_col_with_6_innie = """
        {
        "cages": [
            {
            "coordinates": [
                {
                "x": 0,
                "y": 7
                },
                {
                "x": 0,
                "y": 8
                },
                {
                "x": 1,
                "y": 8
                },
                {
                "x": 2,
                "y": 8
                }
            ],
            "sum": 16
            },
            {
            "coordinates": [
                {
                "x": 0,
                "y": 0
                },
                {
                "x": 0,
                "y": 1
                },
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
                },
                {
                "x": 0,
                "y": 5
                },
                {
                "x": 0,
                "y": 6
                }
            ],
            "sum": 39
            }
        ],
        "cells": []
        }"""

    one_box_with_6_innie = """
        {
        "cages": [
            {
            "coordinates": [
                {
                "x": 1,
                "y": 2
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
                }
            ],
            "sum": 16
            },
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
                },
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
                "x": 0,
                "y": 2
                }
            ],
            "sum": 39
            }
        ],
        "cells": []
        }"""

    def setUp(self):
        self.board = Board()
        self.rule = CageSplittingIO()

    def test_basic_case_row(self):
        self.board.load_json(self.one_row_with_6_innie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.cages), 1)
        self.assertEqual(len(update.cages[0].subcages), 2)
        for c in update.cages:
            self.assertTrue(all(str(coord) in ["H1", "I1", "I2", "I3"] for sc in c.subcages for coord in sc.coordinates))
        self.assertEqual(update.rule_name, "Killer Cage Splitting (Innie/Outie)")
        self.assertEqual(update.explanation, "Row 1 forms a cage which adds to 45, and all cages containing the row except for ['H1', 'I1'] sum to 39, making inferred cage ['H1', 'I1'] sum to 6.")

    def test_basic_case_row_inferred(self):
        self.board.load_json(self.one_row_with_6_innie)
        for cage in self.board.cages:
            if "H1" in [str(c) for c in cage.coordinates]: 
                cage.subcages = [
                    Cage([Coordinates(7,0), Coordinates(8,0), Coordinates(8,1)], 15),
                    Cage([Coordinates(8,2)], 1)]
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.cages), 1)
        self.assertEqual(len(update.cages[0].subcages), 3)
        for c in update.cages:
            self.assertTrue(all(str(coord) in ["H1", "I1", "I2", "I3"] for sc in c.subcages for coord in sc.coordinates))
        self.assertEqual(update.rule_name, "Killer Cage Splitting (Innie/Outie)")
        self.assertEqual(update.explanation, "Row 1 forms a cage which adds to 45, and all cages containing the row except for ['H1', 'I1'] sum to 39, making inferred cage ['H1', 'I1'] sum to 6.")

    def test_basic_case_col(self):
        self.board.load_json(self.one_col_with_6_innie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.cages), 1)
        self.assertEqual(len(update.cages[0].subcages), 2)
        for c in update.cages:
            self.assertTrue(all(str(coord) in ["A8", "A9", "B9", "C9"] for sc in c.subcages for coord in sc.coordinates))
        self.assertEqual(update.rule_name, "Killer Cage Splitting (Innie/Outie)")
        self.assertEqual(update.explanation, "Column A forms a cage which adds to 45, and all cages containing the column except for ['A8', 'A9'] sum to 39, making ['A8', 'A9'] equal to 6.")

    def test_basic_case_col_inferred(self):
        self.board.load_json(self.one_col_with_6_innie)
        for cage in self.board.cages:
            if "A8" in [str(c) for c in cage.coordinates]: 
                cage.subcages = [
                    Cage([Coordinates(0,7), Coordinates(0,8), Coordinates(1,8)], 15),
                    Cage([Coordinates(2,8)], 1)]
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.cages), 1)
        self.assertEqual(len(update.cages[0].subcages), 3)
        for c in update.cages:
            self.assertTrue(all(str(coord) in ["A8", "A9", "B9", "C9"] for sc in c.subcages for coord in sc.coordinates))
        self.assertEqual(update.rule_name, "Killer Cage Splitting (Innie/Outie)")
        self.assertEqual(update.explanation, "Column A forms a cage which adds to 45, and all cages containing the column except for ['A8', 'A9'] sum to 39, making ['A8', 'A9'] equal to 6.")

    def test_basic_case_box(self):
        self.board.load_json(self.one_box_with_6_innie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.cages), 1)
        self.assertEqual(len(update.cages[0].subcages), 2)
        for c in update.cages:
            self.assertTrue(all(str(coord) in ["B3", "C3", "D3", "D4"] for sc in c.subcages for coord in sc.coordinates))
        self.assertEqual(update.rule_name, "Killer Cage Splitting (Innie/Outie)")
        self.assertEqual(update.explanation, "Box (0, 0) forms a cage which adds to 45, and all cages containing the box except for ['B3', 'C3'] sum to 39, making ['B3', 'C3'] equal to 6.")

    def test_basic_case_box_inferred(self):
        self.board.load_json(self.one_box_with_6_innie)
        for cage in self.board.cages:
            if "B3" in [str(c) for c in cage.coordinates]: 
                cage.subcages = [
                    Cage([Coordinates(1,2), Coordinates(2,2), Coordinates(3,2)], 15),
                    Cage([Coordinates(3,3)], 1)]
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.cages), 1)
        self.assertEqual(len(update.cages[0].subcages), 3)
        for c in update.cages:
            self.assertTrue(all(str(coord) in ["B3", "C3", "D3", "D4"] for sc in c.subcages for coord in sc.coordinates))
        self.assertEqual(update.rule_name, "Killer Cage Splitting (Innie/Outie)")
        self.assertEqual(update.explanation, "Box (0, 0) forms a cage which adds to 45, and all cages containing the box except for ['B3', 'C3'] sum to 39, making ['B3', 'C3'] equal to 6.")