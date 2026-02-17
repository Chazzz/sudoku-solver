import unittest
from core.rules.cage_splitting_basic import CageSplittingBasic
from core.board import Board
from core.cage import Cage
from core.coordinates import Coordinates

class TestEasyCombinations(unittest.TestCase):

    one_three_cage = """
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
                }
            ],
            "sum": 3
            }
        ],
        "cells": [
            {
            "x": 0,
            "y": 0,
            "candidates": [
                1
            ]
            },
            {
            "x": 1,
            "y": 0,
            "candidates": [
                2
            ]
            }
        ]
        }"""

    big_16_cage = """
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
                }
            ],
            "sum": 16
            }
        ],
        "cells": [
            {
            "x": 0,
            "y": 0,
            "candidates": [
                1
            ]
            },
            {
            "x": 1,
            "y": 0,
            "candidates": [
                6
            ]
            }
        ]
        }"""

    def setUp(self):
        self.board = Board()
        self.rule = CageSplittingBasic()

    def test_basic_case(self):
        self.board.load_json(self.one_three_cage)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.cages), 1)
        self.assertEqual(len(update.cages[0].subcages), 2)
        for c in update.cages:
                self.assertTrue(all(str(coord) in ["A1", "B1"] for sc in c.subcages for coord in sc.coordinates))
        self.assertEqual(update.rule_name, "Killer Cage Splitting (Basic)")
        self.assertEqual(update.explanation, "Cage ['A1', 'B1'] with sum 3 can be split by having A1 as a separate cage.")

    def test_basic_case_with_subcage(self):
        self.board.load_json(self.one_three_cage)
        for cage in self.board.cages:
            cage.subcages = [Cage([Coordinates(0,0)], 1)]
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.cages), 1)
        for c in update.cages:
            self.assertTrue(all(str(coord) in ["A1", "B1"] for sc in c.subcages for coord in sc.coordinates))
        self.assertEqual(update.rule_name, "Killer Cage Splitting (Basic)")
        self.assertEqual(update.explanation, "Cage ['A1', 'B1'] with sum 3 can be split by having B1 as a separate cage.")

    def test_split_subcage(self):
        self.board.load_json(self.big_16_cage)
        for cage in self.board.cages:
            cage.subcages = [Cage([Coordinates(0,0)], 1), Cage([Coordinates(1,0), Coordinates(2,0)], 15)]
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.cages), 1)
        for c in update.cages:
            self.assertTrue(all(str(coord) in ["A1", "B1", "C1"] for sc in c.subcages for coord in sc.coordinates))
        self.assertEqual(update.rule_name, "Killer Cage Splitting (Basic)")
        self.assertEqual(update.explanation, "Cage ['A1', 'B1', 'C1'] with sum 16 can be split by having B1 as a separate cage.")

    def test_basic_case_filled_in(self):
        self.board.load_json(self.one_three_cage)
        for cage in self.board.cages:
            cage.subcages = [Cage([Coordinates(0,0)], 1), Cage([Coordinates(1,0)], 2)]
        update = self.rule.find_update(self.board)
        self.assertIsNone(update.cages)