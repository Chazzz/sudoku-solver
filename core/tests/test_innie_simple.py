import unittest
from core.rules.innie_simple import InnieSimple
from core.board import Board

class TestInnieSimple(unittest.TestCase):
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

    two_rows_with_6_innie = """
        {
        "cages": [
            {
            "coordinates": [
                {
                "x": 1,
                "y": 0
                },
                {
                "x": 1,
                "y": 1
                }
            ],
            "sum": 17
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
                }
            ],
            "sum": 3
            },
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
                },
                {
                "x": 8,
                "y": 0
                },
                {
                "x": 2,
                "y": 1
                },
                {
                "x": 3,
                "y": 1
                }
            ],
            "sum": 45
            },
            {
            "coordinates": [
                {
                "x": 4,
                "y": 1
                },
                {
                "x": 5,
                "y": 1
                },
                {
                "x": 6,
                "y": 1
                },
                {
                "x": 7,
                "y": 1
                }
            ],
            "sum": 19
            },
            {
            "coordinates": [
                {
                "x": 8,
                "y": 1
                },
                {
                "x": 8,
                "y": 2
                }
            ],
            "sum": 13
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

    two_cols_with_6_innie = """
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
            },
            {
            "coordinates": [
                {
                "x": 0,
                "y": 1
                },
                {
                "x": 1,
                "y": 1
                }
            ],
            "sum": 17
            },
            {
            "coordinates": [
                {
                "x": 0,
                "y": 2
                },
                {
                "x": 1,
                "y": 2
                },
                {
                "x": 0,
                "y": 3
                },
                {
                "x": 1,
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
                },
                {
                "x": 0,
                "y": 8
                }
            ],
            "sum": 45
            },
            {
            "coordinates": [
                {
                "x": 1,
                "y": 4
                },
                {
                "x": 1,
                "y": 5
                },
                {
                "x": 1,
                "y": 6
                },
                {
                "x": 1,
                "y": 7
                }
            ],
            "sum": 19
            },
            {
            "coordinates": [
                {
                "x": 1,
                "y": 8
                },
                {
                "x": 2,
                "y": 8
                }
            ],
            "sum": 13
            }
        ]
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

    two_boxes_with_6_innie = """
        {
        "cages": [
            {
            "coordinates": [
                {
                "x": 5,
                "y": 2
                },
                {
                "x": 5,
                "y": 3
                }
            ],
            "sum": 17
            },
            {
            "coordinates": [
                {
                "x": 4,
                "y": 2
                },
                {
                "x": 4,
                "y": 3
                }
            ],
            "sum": 3
            },
            {
            "coordinates": [
                {
                "x": 3,
                "y": 0
                },
                {
                "x": 3,
                "y": 1
                },
                {
                "x": 3,
                "y": 2
                },
                {
                "x": 3,
                "y": 3
                },
                {
                "x": 3,
                "y": 4
                },
                {
                "x": 4,
                "y": 4
                },
                {
                "x": 5,
                "y": 4
                },
                {
                "x": 3,
                "y": 5
                },
                {
                "x": 4,
                "y": 5
                }
            ],
            "sum": 45
            },
            {
            "coordinates": [
                {
                "x": 4,
                "y": 0
                },
                {
                "x": 5,
                "y": 0
                },
                {
                "x": 4,
                "y": 1
                },
                {
                "x": 5,
                "y": 1
                }
            ],
            "sum": 19
            },
            {
            "coordinates": [
                {
                "x": 5,
                "y": 5
                },
                {
                "x": 6,
                "y": 5
                }
            ],
            "sum": 10
            }
        ]
        }"""

    def setUp(self):
        self.board = Board()
        self.rule = InnieSimple()

    def test_basic_case_row(self):
        self.board.load_json(self.one_row_with_6_innie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "I1")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Innie (1 cell)")
        self.assertEqual(update.explanation, "Row 1 forms a cage which adds to 45, and all cages containing the row except for I1 sum to 39, making I1 equal to 6.")

    def test_multiple_rows(self):
        self.board.load_json(self.two_rows_with_6_innie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "I2")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Innie (1 cell)")
        self.assertEqual(update.explanation, "Rows 1-2 form a cage which adds to 90, and all cages containing the rows except for I2 sum to 84, making I2 equal to 6.")

    def test_basic_case_col(self):
        self.board.load_json(self.one_col_with_6_innie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "A9")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Innie (1 cell)")
        self.assertEqual(update.explanation, "Column A forms a cage which adds to 45, and all cages containing the column except for A9 sum to 39, making A9 equal to 6.")

    def test_multiple_cols(self):
        self.board.load_json(self.two_cols_with_6_innie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "B9")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Innie (1 cell)")
        self.assertEqual(update.explanation, "Columns A-B form a cage which adds to 90, and all cages containing the columns except for B9 sum to 84, making B9 equal to 6.")

    def test_basic_case_box(self):
        self.board.load_json(self.one_box_with_6_innie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "C3")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Innie (1 cell)")
        self.assertEqual(update.explanation, "Box (0, 0) forms a cage which adds to 45, and all cages containing the box except for C3 sum to 39, making C3 equal to 6.")

    def test_multiple_boxes(self):
        self.board.load_json(self.two_boxes_with_6_innie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "F6")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Innie (1 cell)")
        self.assertEqual(update.explanation, "Boxes (1, 0) and (1, 1) form a cage which adds to 90, and all cages containing the boxes except for F6 sum to 84, making F6 equal to 6.")

    def test_innie_filled_in(self):
        self.board.load_json(self.two_boxes_with_6_innie)
        for c in self.board:
            if c.x == 5 and c.y == 5:
                c.candidates = [6]
        update = self.rule.find_update(self.board)
        self.assertIsNone(update.eliminations)

