import unittest
from core.rules.hard_combinations_inferred import HardCombinationsInferred
from core.board import Board
from core.cage import Cage
from core.coordinates import Coordinates

class TestHardCombinationsInferred(unittest.TestCase):

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
            }
        ]
        }"""

    def setUp(self):
        self.board = Board()
        self.rule = HardCombinationsInferred()

    def test_basic_case(self):
        self.board.load_json(self.one_three_cage)
        for cage in self.board.cages:
            cage.subcages = [Cage([Coordinates(0,0)], 1), Cage([Coordinates(1,0)], 2)]
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertTrue(str(e) in ["B1"])
            self.assertEqual(e.candidates, [1, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Hard Combinations (Inferred)")
        self.assertEqual(update.explanation, "The following values are never used to form a valid sum in inferred cage ['B1'] with sum 2: 1 at B1, 3 at B1, 4 at B1, 5 at B1, 6 at B1, 7 at B1, 8 at B1, and 9 at B1.")
