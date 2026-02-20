import unittest
from core.rules.innie_advanced import InnieAdvanced
from core.board import Board

class TestInnieAdvanced(unittest.TestCase):
    maxDiff = None

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

    two_rows_with_6_innie_2_cell = """
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
                "x": 8,
                "y": 1
                },
                {
                "x": 8,
                "y": 2
                }
            ],
            "sum": 13
            },
            {
            "coordinates": [
                {
                "x": 7,
                "y": 1
                },
                {
                "x": 7,
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
                "x": 5,
                "y": 1
                },
                {
                "x": 6,
                "y": 1
                }
            ],
            "sum": 19
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
    
    two_cols_with_6_innie_2_cell = """
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
                "y": 8
                },
                {
                "x": 2,
                "y": 8
                }
            ],
            "sum": 13
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
                }
            ],
            "sum": 19
            },
            {
            "coordinates": [
                {
                "x": 1,
                "y": 7
                },
                {
                "x": 2,
                "y": 7
                }
            ],
            "sum": 9
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

    two_boxes_with_6_innie_2_cell = """
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
                "x": 5,
                "y": 5
                },
                {
                "x": 6,
                "y": 5
                }
            ],
            "sum": 10
            },
            {
            "coordinates": [
                {
                "x": 4,
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
                "y": 0
                },
                {
                "x": 6,
                "y": 0
                }
            ],
            "sum": 10
            }
        ],
        "cells": []
        }"""

    def setUp(self):
        self.board = Board()
        self.rule = InnieAdvanced()

    def test_basic_case_row(self):
        self.board.load_json(self.one_row_with_6_innie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "I1")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Innie (2+ cells)")
        self.assertEqual(update.explanation, "Row 1 forms a cage which adds to 45, and all cages containing the row except for ['I1'] sum to 39, making cells ['I1'] sum to 6. The following values are never used to form a valid sum in cells ['I1']: 1 at I1, 2 at I1, 3 at I1, 4 at I1, 5 at I1, 7 at I1, 8 at I1, and 9 at I1.")

    def test_multiple_rows(self):
        self.board.load_json(self.two_rows_with_6_innie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "I2")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Innie (2+ cells)")
        self.assertEqual(update.explanation, "Rows 1-2 form a cage which adds to 90, and all cages containing the rows except for ['I2'] sum to 84, making cells ['I2'] sum to 6. The following values are never used to form a valid sum in cells ['I2']: 1 at I2, 2 at I2, 3 at I2, 4 at I2, 5 at I2, 7 at I2, 8 at I2, and 9 at I2.")

    def test_multiple_rows_and_cells(self):
        self.board.load_json(self.two_rows_with_6_innie_2_cell)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 2) 
        for e in update.eliminations:
            self.assertTrue(str(e) in ["H2", "I2"])
            self.assertEqual(e.candidates, [3, 6, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Innie (2+ cells)")
        self.assertEqual(update.explanation, "Rows 1-2 form a cage which adds to 90, and all cages containing the rows except for ['I2', 'H2'] sum to 84, making cells ['I2', 'H2'] sum to 6. The following values are never used to form a valid sum in cells ['I2', 'H2']: 3 at H2, 6 at H2, 7 at H2, 8 at H2, 9 at H2, 3 at I2, 6 at I2, 7 at I2, 8 at I2, and 9 at I2.")

    def test_basic_case_col(self):
        self.board.load_json(self.one_col_with_6_innie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "A9")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Innie (2+ cells)")
        self.assertEqual(update.explanation, "Column A forms a cage which adds to 45, and all cages containing the column except for ['A9'] sum to 39, making cells ['A9'] sum to 6. The following values are never used to form a valid sum in cells ['A9']: 1 at A9, 2 at A9, 3 at A9, 4 at A9, 5 at A9, 7 at A9, 8 at A9, and 9 at A9.")

    def test_multiple_cols(self):
        self.board.load_json(self.two_cols_with_6_innie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "B9")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Innie (2+ cells)")
        self.assertEqual(update.explanation, "Columns A-B form a cage which adds to 90, and all cages containing the columns except for ['B9'] sum to 84, making cells ['B9'] sum to 6. The following values are never used to form a valid sum in cells ['B9']: 1 at B9, 2 at B9, 3 at B9, 4 at B9, 5 at B9, 7 at B9, 8 at B9, and 9 at B9.")

    def test_multiple_cols_and_cells(self):
        self.board.load_json(self.two_cols_with_6_innie_2_cell)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 2) 
        for e in update.eliminations:
            self.assertTrue(str(e) in ["B8", "B9"])
            self.assertEqual(e.candidates, [3, 6, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Innie (2+ cells)")
        self.assertEqual(update.explanation, "Columns A-B form a cage which adds to 90, and all cages containing the columns except for ['B9', 'B8'] sum to 84, making cells ['B9', 'B8'] sum to 6. The following values are never used to form a valid sum in cells ['B9', 'B8']: 3 at B8, 6 at B8, 7 at B8, 8 at B8, 9 at B8, 3 at B9, 6 at B9, 7 at B9, 8 at B9, and 9 at B9.")

    def test_basic_case_box(self):
        self.board.load_json(self.one_box_with_6_innie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "C3")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Innie (2+ cells)")
        self.assertEqual(update.explanation, "Box (0, 0) forms a cage which adds to 45, and all cages containing the box except for ['C3'] sum to 39, making cells ['C3'] sum to 6. The following values are never used to form a valid sum in cells ['C3']: 1 at C3, 2 at C3, 3 at C3, 4 at C3, 5 at C3, 7 at C3, 8 at C3, and 9 at C3.")

    def test_multiple_boxes(self):
        self.board.load_json(self.two_boxes_with_6_innie)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 1) 
        for e in update.eliminations:
            self.assertEqual(str(e), "F6")
            self.assertEqual(e.candidates, [1, 2, 3, 4, 5, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Innie (2+ cells)")
        self.assertEqual(update.explanation, "Boxes (1, 0) and (1, 1) form a cage which adds to 90, and all cages containing the boxes except for ['F6'] sum to 84, making cells ['F6'] sum to 6. The following values are never used to form a valid sum in cells ['F6']: 1 at F6, 2 at F6, 3 at F6, 4 at F6, 5 at F6, 7 at F6, 8 at F6, and 9 at F6.")

    def test_multiple_boxes_and_cells(self):
        self.board.load_json(self.two_boxes_with_6_innie_2_cell)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.eliminations), 2) 
        for e in update.eliminations:
            self.assertTrue(str(e) in ["F1", "F6"])
            self.assertEqual(e.candidates, [3, 6, 7, 8, 9])
        self.assertEqual(update.rule_name, "Killer Innie (2+ cells)")
        self.assertEqual(update.explanation, "Boxes (1, 0) and (1, 1) form a cage which adds to 90, and all cages containing the boxes except for ['F6', 'F1'] sum to 84, making cells ['F6', 'F1'] sum to 6. The following values are never used to form a valid sum in cells ['F6', 'F1']: 3 at F1, 6 at F1, 7 at F1, 8 at F1, 9 at F1, 3 at F6, 6 at F6, 7 at F6, 8 at F6, and 9 at F6.")


    def test_innie_filled_in(self):
        self.board.load_json(self.two_boxes_with_6_innie)
        for c in self.board:
            if c.x == 5 and c.y == 5:
                c.candidates = [6]
            elif c.x // 3 == 1 and c.y // 3 == 1:
                c.candidates = [1, 2, 3, 4, 5, 7, 8, 9]
        update = self.rule.find_update(self.board)
        self.assertIsNone(update.eliminations)

