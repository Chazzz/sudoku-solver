import unittest
from core.rules.outie_advanced import OutieAdvancedTemplate
from core.board import Board

class TestOutieAdvanced(unittest.TestCase):
    maxDiff = None

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
        self.rule = OutieAdvancedTemplate()
        self.rule.min_outie = 1
        self.rule.max_outie = 100
    
    def test_basic_case(self):
        self.board.load_json(self.one_row_with_6_outie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "I2")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Outie (2+ cells)")
        self.assertEqual(update.explanation, "Row 1 forms a cage which adds to 45, and all cages containing the row plus ['I2'] sum to 51, making cells ['I2'] sum to 6. The following values are never used to form a valid sum in cells ['I2']: 1 at I2, 2 at I2, 3 at I2, 4 at I2, 5 at I2, 7 at I2, 8 at I2, and 9 at I2.")

    def test_missing_cage(self):
        self.board.load_json(self.one_row_false_6_outie)
        update = self.rule.find_update(self.board)
        self.assertIsNone(update.eliminations)
    
    def test_row_multiple_cells(self):
        self.board.load_json(self.two_rows_with_6_outie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 4) 
        for e in update.eliminations:
            if str(e) == "I3":
                self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
            else:
                self.assertTrue(str(e) in ["G2", "H2", "I2"])
                self.assertEqual(e.candidates, [6])
        self.assertEqual(update.rule_name, "Killer Outie (2+ cells)")
        self.assertEqual(update.explanation, "Row 1 forms a cage which adds to 45, and all cages containing the row plus ['I2', 'I3', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'] sum to 96, making cells ['I2', 'I3', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'] sum to 51. The following values are never used to form a valid sum in cells ['I2', 'I3', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2']: 6 at G2, 6 at H2, 6 at I2, 1 at I3, 2 at I3, 3 at I3, 4 at I3, 5 at I3, 7 at I3, 8 at I3, and 9 at I3.")

    def test_basic_case_col(self):
        self.board.load_json(self.one_col_with_6_outie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "B9")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Outie (2+ cells)")
        self.assertEqual(update.explanation, "Column A forms a cage which adds to 45, and all cages containing the column plus ['B9'] sum to 51, making cells ['B9'] sum to 6. The following values are never used to form a valid sum in cells ['B9']: 1 at B9, 2 at B9, 3 at B9, 4 at B9, 5 at B9, 7 at B9, 8 at B9, and 9 at B9.")

    def test_missing_cage_col(self):
        self.board.load_json(self.one_col_false_6_outie)
        update = self.rule.find_update(self.board)
        self.assertIsNone(update.eliminations)
    
    def test_col_multiple_cells(self):
        self.board.load_json(self.two_cols_with_6_outie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 4) 
        for e in update.eliminations:
            if str(e) == "C9":
                self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
            else:
                self.assertTrue(str(e) in ["B7", "B8", "B9"])
                self.assertEqual(e.candidates, [6])
        self.assertEqual(update.rule_name, "Killer Outie (2+ cells)")
        self.assertEqual(update.explanation, "Column A forms a cage which adds to 45, and all cages containing the column plus ['B9', 'C9', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8'] sum to 96, making cells ['B9', 'C9', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8'] sum to 51. The following values are never used to form a valid sum in cells ['B9', 'C9', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8']: 6 at B7, 6 at B8, 6 at B9, 1 at C9, 2 at C9, 3 at C9, 4 at C9, 5 at C9, 7 at C9, 8 at C9, and 9 at C9.")

    def test_basic_case_box(self):
        self.board.load_json(self.one_box_with_6_outie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "D3")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Outie (2+ cells)")
        self.assertEqual(update.explanation, "Box (0, 0) forms a cage which adds to 45, and all cages containing the box plus ['D3'] sum to 51, making cells ['D3'] sum to 6. The following values are never used to form a valid sum in cells ['D3']: 1 at D3, 2 at D3, 3 at D3, 4 at D3, 5 at D3, 7 at D3, 8 at D3, and 9 at D3.")

    def test_missing_cage_box(self):
        self.board.load_json(self.one_box_false_6_outie)
        update = self.rule.find_update(self.board)
        self.assertIsNone(update.eliminations)
    
    def test_boxes_multiple_cells(self):
        self.board.load_json(self.two_boxes_with_6_outie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "C3")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Outie (2+ cells)")
        self.assertEqual(update.explanation, "Box (1, 0) forms a cage which adds to 45, and all cages containing the box plus ['C3', 'D4', 'E4', 'D5', 'E5', 'D6', 'E6', 'F6', 'F4', 'F5'] sum to 96, making cells ['C3', 'D4', 'E4', 'D5', 'E5', 'D6', 'E6', 'F6', 'F4', 'F5'] sum to 51. The following values are never used to form a valid sum in cells ['C3', 'D4', 'E4', 'D5', 'E5', 'D6', 'E6', 'F6', 'F4', 'F5']: 1 at C3, 2 at C3, 3 at C3, 4 at C3, 5 at C3, 7 at C3, 8 at C3, and 9 at C3.")

    def test_outie_filled_in(self):
        self.board.load_json(self.two_boxes_with_6_outie)
        for c in self.board:
            if c.x == 2 and c.y == 2:
                c.candidates = [6]
            if c.x == 2 and c.y == 2:
                c.candidates = [6]
            if str(c) in ["D1", "D2", "E1", "E2", "E3", "F1", "F2", "F3"]:
                c.candidates = [1, 2, 4, 5, 6, 7, 8, 9]
        update = self.rule.find_update(self.board)
        self.assertIsNone(update.eliminations)