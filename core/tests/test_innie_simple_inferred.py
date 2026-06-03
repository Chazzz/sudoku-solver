import unittest
from core.rules.innie_simple_inferred import InnieSimpleInferred
from core.board import Board
from core.cage import Cage
from core.coordinates import Coordinates

class TestInnieSimpleInferred(unittest.TestCase):
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
                },
                {
                "x": 7,
                "y": 0
                }
            ],
            "sum": 39
            },
            {
            "coordinates": [
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
            "sum": 20
            }
        ]
        }"""

    one_row_with_6_innie_inferred = """
        {
        "cages": [
            {
            "coordinates": [
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
            "sum": 20
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
            "sum": 38
            },
            {
            "coordinates": [
                {
                "x": 7,
                "y": 0
                },
                {
                "x": 7,
                "y": 1
                },
                {
                "x": 7,
                "y": 2
                }
            ],
            "sum": 16
            }
        ],
        "cells": [
            {
            "x": 7,
            "y": 0,
            "candidates": [
                1
            ]
            }
        ]
        }"""

    one_col_with_6_innie = """
        {
        "cages": [
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
                },
                {
                "x": 0,
                "y": 7
                }
            ],
            "sum": 39
            },
            {
            "coordinates": [
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
            "sum": 20
            }
        ]
        }"""

    one_col_with_6_innie_inferred = """
        {
        "cages": [
            {
            "coordinates": [
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
            "sum": 20
            },
            {
            "coordinates": [
                {
                "x": 0,
                "y": 7
                },
                {
                "x": 1,
                "y": 7
                },
                {
                "x": 2,
                "y": 7
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
            "sum": 38
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
                },
                {
                "x": 1,
                "y": 2
                }
            ],
            "sum": 39
            },
            {
            "coordinates": [
                {
                "x": 2,
                "y": 2
                },
                {
                "x": 3,
                "y": 2
                }
            ],
            "sum": 9
            }
        ]
        }"""

    one_box_with_6_innie_inferred = """
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
                }
            ],
            "sum": 9
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
            "sum": 38
            },
            {
            "coordinates": [
                {
                "x": 1,
                "y": 2
                },
                {
                "x": 1,
                "y": 3
                },
                {
                "x": 1,
                "y": 4
                }
            ],
            "sum": 16
            }
        ],
        "cells": []
        }"""

    one_row_with_6_innie_inferred_virtual = """
        {
        "cages": [
            {
            "coordinates": [
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
            "sum": 20
            }
        ],
        "virtual_cages": [
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
            "sum": 38
            },
            {
            "coordinates": [
                {
                "x": 7,
                "y": 0
                },
                {
                "x": 7,
                "y": 1
                },
                {
                "x": 7,
                "y": 2
                }
            ],
            "sum": 16
            }
        ],
        "cells": [
            {
            "x": 7,
            "y": 0,
            "candidates": [
                1
            ]
            }
        ]
        }"""


    def setUp(self):
        self.board = Board()
        self.rule = InnieSimpleInferred()

    def test_basic_case_row_no_subcages(self):
        self.board.load_json(self.one_row_with_6_innie)
        update = self.rule.find_update(self.board)
        self.assertIsNone(update.eliminations) 

    def test_basic_case_row(self):
        self.board.load_json(self.one_row_with_6_innie_inferred)
        for cage in self.board.cages:
            if "H1" in [str(c) for c in cage.coordinates]: 
                cage.subcages = [Cage([Coordinates(7,0)], 1), Cage([Coordinates(7,1), Coordinates(7,2)], 15)]
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "I1")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Innie (1 cell, inferred)")
        self.assertEqual(update.explanation, "Row 1 forms a cage which adds to 45, and all cages containing the row except for I1 sum to 39, making I1 equal to 6.")

    def test_basic_case_col(self):
        self.board.load_json(self.one_col_with_6_innie)
        update = self.rule.find_update(self.board)
        self.assertIsNone(update.eliminations)

    def test_basic_case_col_inferred(self):
        self.board.load_json(self.one_col_with_6_innie_inferred)
        for cage in self.board.cages:
            if "A8" in [str(c) for c in cage.coordinates]: 
                cage.subcages = [Cage([Coordinates(0,7)], 1), Cage([Coordinates(1,7), Coordinates(2,7)], 15)]
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "A9")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Innie (1 cell, inferred)")
        self.assertEqual(update.explanation, "Column A forms a cage which adds to 45, and all cages containing the column except for A9 sum to 39, making A9 equal to 6.")

    def test_basic_case_box(self):
        self.board.load_json(self.one_box_with_6_innie)
        update = self.rule.find_update(self.board)
        self.assertIsNone(update.eliminations)
    
    def test_basic_case_box_inferred(self):
        self.board.load_json(self.one_box_with_6_innie_inferred)
        for cage in self.board.cages:
            if "B3" in [str(c) for c in cage.coordinates]: 
                cage.subcages = [Cage([Coordinates(1,2)], 1), Cage([Coordinates(1,3), Coordinates(1,4)], 15)]
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "C3")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Innie (1 cell, inferred)")
        self.assertEqual(update.explanation, "Box (0, 0) forms a cage which adds to 45, and all cages containing the box except for C3 sum to 39, making C3 equal to 6.")

