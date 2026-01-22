import unittest
from core.rules.outie_simple import OutieSimple
from core.board import Board

class TestOutieSimple(unittest.TestCase):
    one_row_with_6_outie = """
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
            "sum": 42
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
                }
            ],
            "sum": 9
            }
        ]
        }"""
    
    # 0, 0 is uncaged
    one_row_false_6_outie = """
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
            "sum": 9
            },
            {
            "coordinates": [
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
            "sum": 42
            }
        ]
        }"""
    
    two_rows_with_6_outie = """
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
            "sum": 9
            },
            {
            "coordinates": [
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
            "sum": 42
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
                "x": 1,
                "y": 1
                },
                {
                "x": 2,
                "y": 1
                },
                {
                "x": 3,
                "y": 1
                },
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
            "sum": 45
            }
        ]
        }"""

    one_col_with_6_outie = """
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
            "sum": 42
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
                }
            ],
            "sum": 9
            }
        ]
        }"""

    one_col_false_6_outie = """
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
                }
            ],
            "sum": 9
            },
            {
            "coordinates": [
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
            "sum": 42
            }
        ]
        }"""

    two_cols_with_6_outie = """
        {
        "cages": [
            {
            "coordinates": [
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
            "sum": 42
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
                "x": 1,
                "y": 1
                },
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
            "sum": 45
            }
        ]
        }"""

    one_box_with_6_outie = """
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
                },
                {
                "x": 1,
                "y": 2
                }
            ],
            "sum": 42
            }
        ]
        }"""

    one_box_false_6_outie = """
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
            "sum": 42
            }
        ]
        }"""

    two_boxes_with_6_outie = """
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
                "x": 4,
                "y": 1
                },
                {
                "x": 4,
                "y": 2
                },
                {
                "x": 3,
                "y": 3
                },
                {
                "x": 4,
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
                "x": 3,
                "y": 5
                },
                {
                "x": 4,
                "y": 5
                },
                {
                "x": 5,
                "y": 5
                }
            ],
            "sum": 45
            },
            {
            "coordinates": [
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
                "x": 3,
                "y": 1
                },
                {
                "x": 5,
                "y": 1
                },
                {
                "x": 5,
                "y": 2
                },
                {
                "x": 5,
                "y": 3
                },
                {
                "x": 5,
                "y": 4
                }
            ],
            "sum": 42
            }
        ]
        }"""

    def setUp(self):
        self.board = Board()
        self.rule = OutieSimple()
    
    def test_basic_case(self):
        self.board.load_json(self.one_row_with_6_outie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "I2")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Outie (1 cell)")
        self.assertEqual(update.explanation, "Row 1 forms a cage which adds to 45, and all cages containing the row sum to 51, making I2, the only outside cell, equal to 6.")

    def test_missing_cage(self):
        self.board.load_json(self.one_row_false_6_outie)
        update = self.rule.find_update(self.board)
        self.assertIsNone(update.eliminations)
    
    def test_multiple_rows(self):
        self.board.load_json(self.two_rows_with_6_outie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "I3")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Outie (1 cell)")
        self.assertEqual(update.explanation, "Rows 1-2 form a cage which adds to 90, and all cages containing the rows sum to 96, making I3, the only outside cell, equal to 6.")

    def test_basic_case_col(self):
        self.board.load_json(self.one_col_with_6_outie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "B9")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Outie (1 cell)")
        self.assertEqual(update.explanation, "Column A forms a cage which adds to 45, and all cages containing the column sum to 51, making B9, the only outside cell, equal to 6.")

    def test_missing_cage_col(self):
        self.board.load_json(self.one_col_false_6_outie)
        update = self.rule.find_update(self.board)
        self.assertIsNone(update.eliminations)
    
    def test_multiple_cols(self):
        self.board.load_json(self.two_cols_with_6_outie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "C9")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Outie (1 cell)")
        self.assertEqual(update.explanation, "Columns A-B form a cage which adds to 90, and all cages containing the columns sum to 96, making C9, the only outside cell, equal to 6.")

    def test_basic_case_box(self):
        self.board.load_json(self.one_box_with_6_outie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "D3")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Outie (1 cell)")
        self.assertEqual(update.explanation, "Box (0, 0) forms a cage which adds to 45, and all cages containing the box sum to 51, making D3, the only outside cell, equal to 6.")

    def test_missing_cage_box(self):
        self.board.load_json(self.one_box_false_6_outie)
        update = self.rule.find_update(self.board)
        self.assertIsNone(update.eliminations)
    
    def test_multiple_boxes(self):
        self.board.load_json(self.two_boxes_with_6_outie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "C3")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Outie (1 cell)")
        self.assertEqual(update.explanation, "Boxes (1, 0) and (1, 1) form a cage which adds to 90, and all cages containing the boxes sum to 96, making C3, the only outside cell, equal to 6.")
