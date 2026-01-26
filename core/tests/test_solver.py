import unittest
from core.board import Board
from core.solver import Solver

class TestBoard(unittest.TestCase):
    puzzle_open_cages = """
        {
        "cages": [
            {
            "coordinates": [
                {
                "x": 0,
                "y": 5
                },
                {
                "x": 0,
                "y": 4
                }
            ],
            "sum": 11
            },
            {
            "coordinates": [
                {
                "x": 6,
                "y": 8
                },
                {
                "x": 7,
                "y": 8
                }
            ],
            "sum": 10
            },
            {
            "coordinates": [
                {
                "x": 6,
                "y": 5
                },
                {
                "x": 6,
                "y": 6
                }
            ],
            "sum": 8
            },
            {
            "coordinates": [
                {
                "x": 7,
                "y": 1
                },
                {
                "x": 7,
                "y": 0
                }
            ],
            "sum": 14
            },
            {
            "coordinates": [
                {
                "x": 0,
                "y": 6
                },
                {
                "x": 0,
                "y": 7
                }
            ],
            "sum": 15
            },
            {
            "coordinates": [
                {
                "x": 2,
                "y": 1
                },
                {
                "x": 2,
                "y": 2
                }
            ],
            "sum": 15
            },
            {
            "coordinates": [
                {
                "x": 5,
                "y": 6
                },
                {
                "x": 5,
                "y": 5
                }
            ],
            "sum": 6
            },
            {
            "coordinates": [
                {
                "x": 7,
                "y": 7
                },
                {
                "x": 6,
                "y": 7
                }
            ],
            "sum": 11
            },
            {
            "coordinates": [
                {
                "x": 2,
                "y": 3
                },
                {
                "x": 3,
                "y": 3
                }
            ],
            "sum": 11
            },
            {
            "coordinates": [
                {
                "x": 4,
                "y": 6
                },
                {
                "x": 3,
                "y": 6
                }
            ],
            "sum": 12
            },
            {
            "coordinates": [
                {
                "x": 7,
                "y": 5
                },
                {
                "x": 7,
                "y": 4
                }
            ],
            "sum": 6
            },
            {
            "coordinates": [
                {
                "x": 2,
                "y": 5
                },
                {
                "x": 2,
                "y": 6
                }
            ],
            "sum": 3
            },
            {
            "coordinates": [
                {
                "x": 6,
                "y": 3
                },
                {
                "x": 6,
                "y": 4
                }
            ],
            "sum": 8
            },
            {
            "coordinates": [
                {
                "x": 0,
                "y": 3
                },
                {
                "x": 0,
                "y": 2
                }
            ],
            "sum": 7
            },
            {
            "coordinates": [
                {
                "x": 3,
                "y": 1
                },
                {
                "x": 3,
                "y": 0
                }
            ],
            "sum": 14
            },
            {
            "coordinates": [
                {
                "x": 8,
                "y": 7
                },
                {
                "x": 8,
                "y": 6
                }
            ],
            "sum": 10
            },
            {
            "coordinates": [
                {
                "x": 4,
                "y": 1
                },
                {
                "x": 4,
                "y": 0
                }
            ],
            "sum": 10
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
            "sum": 5
            },
            {
            "coordinates": [
                {
                "x": 5,
                "y": 8
                },
                {
                "x": 4,
                "y": 8
                }
            ],
            "sum": 6
            },
            {
            "coordinates": [
                {
                "x": 5,
                "y": 4
                },
                {
                "x": 5,
                "y": 3
                }
            ],
            "sum": 11
            },
            {
            "coordinates": [
                {
                "x": 5,
                "y": 0
                },
                {
                "x": 5,
                "y": 1
                }
            ],
            "sum": 11
            },
            {
            "coordinates": [
                {
                "x": 1,
                "y": 6
                },
                {
                "x": 1,
                "y": 7
                }
            ],
            "sum": 8
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
                }
            ],
            "sum": 6
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
                "x": 7,
                "y": 6
                }
            ],
            "sum": 3
            },
            {
            "coordinates": [
                {
                "x": 4,
                "y": 7
                },
                {
                "x": 3,
                "y": 7
                }
            ],
            "sum": 9
            },
            {
            "coordinates": [
                {
                "x": 1,
                "y": 4
                },
                {
                "x": 1,
                "y": 3
                }
            ],
            "sum": 4
            },
            {
            "coordinates": [
                {
                "x": 2,
                "y": 4
                },
                {
                "x": 3,
                "y": 4
                }
            ],
            "sum": 15
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
            "sum": 13
            },
            {
            "coordinates": [
                {
                "x": 3,
                "y": 2
                }
            ],
            "sum": 2
            },
            {
            "coordinates": [
                {
                "x": 7,
                "y": 3
                },
                {
                "x": 8,
                "y": 3
                }
            ],
            "sum": 16
            },
            {
            "coordinates": [
                {
                "x": 8,
                "y": 4
                },
                {
                "x": 8,
                "y": 5
                }
            ],
            "sum": 12
            },
            {
            "coordinates": [
                {
                "x": 5,
                "y": 2
                },
                {
                "x": 6,
                "y": 2
                }
            ],
            "sum": 16
            },
            {
            "coordinates": [
                {
                "x": 2,
                "y": 0
                }
            ],
            "sum": 4
            },
            {
            "coordinates": [
                {
                "x": 1,
                "y": 2
                },
                {
                "x": 1,
                "y": 1
                }
            ],
            "sum": 15
            },
            {
            "coordinates": [
                {
                "x": 6,
                "y": 1
                },
                {
                "x": 6,
                "y": 0
                }
            ],
            "sum": 8
            },
            {
            "coordinates": [
                {
                "x": 8,
                "y": 8
                }
            ],
            "sum": 6
            },
            {
            "coordinates": [
                {
                "x": 0,
                "y": 1
                }
            ],
            "sum": 2
            },
            {
            "coordinates": [
                {
                "x": 5,
                "y": 7
                }
            ],
            "sum": 9
            },
            {
            "coordinates": [
                {
                "x": 3,
                "y": 8
                },
                {
                "x": 2,
                "y": 8
                }
            ],
            "sum": 10
            },
            {
            "coordinates": [
                {
                "x": 4,
                "y": 5
                },
                {
                "x": 3,
                "y": 5
                }
            ],
            "sum": 8
            },
            {
            "coordinates": [
                {
                "x": 2,
                "y": 7
                }
            ],
            "sum": 5
            },
            {
            "coordinates": [
                {
                "x": 8,
                "y": 2
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
                "x": 1,
                "y": 5
                }
            ],
            "sum": 9
            },
            {
            "coordinates": [
                {
                "x": 4,
                "y": 4
                }
            ],
            "sum": 9
            }
        ]
        }"""
    
    puzzle_open_cells = """
        {
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
                5
            ]
            },
            {
            "x": 2,
            "y": 0,
            "candidates": [
                4
            ]
            },
            {
            "x": 3,
            "y": 0,
            "candidates": [
                9
            ]
            },
            {
            "x": 4,
            "y": 0,
            "candidates": [
                6
            ]
            },
            {
            "x": 5,
            "y": 0,
            "candidates": [
                3
            ]
            },
            {
            "x": 6,
            "y": 0,
            "candidates": [
                7
            ]
            },
            {
            "x": 7,
            "y": 0,
            "candidates": [
                8
            ]
            },
            {
            "x": 8,
            "y": 0,
            "candidates": [
                2
            ]
            },
            {
            "x": 0,
            "y": 1,
            "candidates": [
                2
            ]
            },
            {
            "x": 1,
            "y": 1,
            "candidates": [
                7
            ]
            },
            {
            "x": 2,
            "y": 1,
            "candidates": [
                9
            ]
            },
            {
            "x": 3,
            "y": 1,
            "candidates": [
                5
            ]
            },
            {
            "x": 4,
            "y": 1,
            "candidates": [
                4
            ]
            },
            {
            "x": 5,
            "y": 1,
            "candidates": [
                8
            ]
            },
            {
            "x": 6,
            "y": 1,
            "candidates": [
                1
            ]
            },
            {
            "x": 7,
            "y": 1,
            "candidates": [
                6
            ]
            },
            {
            "x": 8,
            "y": 1,
            "candidates": [
                3
            ]
            },
            {
            "x": 0,
            "y": 2,
            "candidates": [
                3
            ]
            },
            {
            "x": 1,
            "y": 2,
            "candidates": [
                8
            ]
            },
            {
            "x": 2,
            "y": 2,
            "candidates": [
                6
            ]
            },
            {
            "x": 3,
            "y": 2,
            "candidates": [
                2
            ]
            },
            {
            "x": 4,
            "y": 2,
            "candidates": [
                1
            ]
            },
            {
            "x": 5,
            "y": 2,
            "candidates": [
                7
            ]
            },
            {
            "x": 6,
            "y": 2,
            "candidates": [
                9
            ]
            },
            {
            "x": 7,
            "y": 2,
            "candidates": [
                4
            ]
            },
            {
            "x": 8,
            "y": 2,
            "candidates": [
                5
            ]
            },
            {
            "x": 0,
            "y": 3,
            "candidates": [
                4
            ]
            },
            {
            "x": 1,
            "y": 3,
            "candidates": [
                1
            ]
            },
            {
            "x": 2,
            "y": 3,
            "candidates": [
                8
            ]
            },
            {
            "x": 3,
            "y": 3,
            "candidates": [
                3
            ]
            },
            {
            "x": 4,
            "y": 3,
            "candidates": [
                2
            ]
            },
            {
            "x": 5,
            "y": 3,
            "candidates": [
                5
            ]
            },
            {
            "x": 6,
            "y": 3,
            "candidates": [
                6
            ]
            },
            {
            "x": 7,
            "y": 3,
            "candidates": [
                9
            ]
            },
            {
            "x": 8,
            "y": 3,
            "candidates": [
                7
            ]
            },
            {
            "x": 0,
            "y": 4,
            "candidates": [
                5
            ]
            },
            {
            "x": 1,
            "y": 4,
            "candidates": [
                3
            ]
            },
            {
            "x": 2,
            "y": 4,
            "candidates": [
                7
            ]
            },
            {
            "x": 3,
            "y": 4,
            "candidates": [
                8
            ]
            },
            {
            "x": 4,
            "y": 4,
            "candidates": [
                9
            ]
            },
            {
            "x": 5,
            "y": 4,
            "candidates": [
                6
            ]
            },
            {
            "x": 6,
            "y": 4,
            "candidates": [
                2
            ]
            },
            {
            "x": 7,
            "y": 4,
            "candidates": [
                1
            ]
            },
            {
            "x": 8,
            "y": 4,
            "candidates": [
                4
            ]
            },
            {
            "x": 0,
            "y": 5,
            "candidates": [
                6
            ]
            },
            {
            "x": 1,
            "y": 5,
            "candidates": [
                9
            ]
            },
            {
            "x": 2,
            "y": 5,
            "candidates": [
                2
            ]
            },
            {
            "x": 3,
            "y": 5,
            "candidates": [
                1
            ]
            },
            {
            "x": 4,
            "y": 5,
            "candidates": [
                7
            ]
            },
            {
            "x": 5,
            "y": 5,
            "candidates": [
                4
            ]
            },
            {
            "x": 6,
            "y": 5,
            "candidates": [
                3
            ]
            },
            {
            "x": 7,
            "y": 5,
            "candidates": [
                5
            ]
            },
            {
            "x": 8,
            "y": 5,
            "candidates": [
                8
            ]
            },
            {
            "x": 0,
            "y": 6,
            "candidates": [
                7
            ]
            },
            {
            "x": 1,
            "y": 6,
            "candidates": [
                6
            ]
            },
            {
            "x": 2,
            "y": 6,
            "candidates": [
                1
            ]
            },
            {
            "x": 3,
            "y": 6,
            "candidates": [
                4
            ]
            },
            {
            "x": 4,
            "y": 6,
            "candidates": [
                8
            ]
            },
            {
            "x": 5,
            "y": 6,
            "candidates": [
                2
            ]
            },
            {
            "x": 6,
            "y": 6,
            "candidates": [
                5
            ]
            },
            {
            "x": 7,
            "y": 6,
            "candidates": [
                3
            ]
            },
            {
            "x": 8,
            "y": 6,
            "candidates": [
                9
            ]
            },
            {
            "x": 0,
            "y": 7,
            "candidates": [
                8
            ]
            },
            {
            "x": 1,
            "y": 7,
            "candidates": [
                2
            ]
            },
            {
            "x": 2,
            "y": 7,
            "candidates": [
                5
            ]
            },
            {
            "x": 3,
            "y": 7,
            "candidates": [
                6
            ]
            },
            {
            "x": 4,
            "y": 7,
            "candidates": [
                3
            ]
            },
            {
            "x": 5,
            "y": 7,
            "candidates": [
                9
            ]
            },
            {
            "x": 6,
            "y": 7,
            "candidates": [
                4
            ]
            },
            {
            "x": 7,
            "y": 7,
            "candidates": [
                7
            ]
            },
            {
            "x": 8,
            "y": 7,
            "candidates": [
                1
            ]
            },
            {
            "x": 0,
            "y": 8,
            "candidates": [
                9
            ]
            },
            {
            "x": 1,
            "y": 8,
            "candidates": [
                4
            ]
            },
            {
            "x": 2,
            "y": 8,
            "candidates": [
                3
            ]
            },
            {
            "x": 3,
            "y": 8,
            "candidates": [
                7
            ]
            },
            {
            "x": 4,
            "y": 8,
            "candidates": [
                5
            ]
            },
            {
            "x": 5,
            "y": 8,
            "candidates": [
                1
            ]
            },
            {
            "x": 6,
            "y": 8,
            "candidates": [
                8
            ]
            },
            {
            "x": 7,
            "y": 8,
            "candidates": [
                2
            ]
            },
            {
            "x": 8,
            "y": 8,
            "candidates": [
                6
            ]
            }
        ]
        }"""

    def setUp(self):
        self.board_master = Board()
        self.board_master.load_json(self.puzzle_open_cells)

        self.board = Board()
        self.board.load_json(self.puzzle_open_cages)
        self.assertEqual(sum(c.sum for c in self.board.cages), 405)
        self.solver = Solver()
    
    # def test_solver_debug(self):
    #     # print(f"Solving puzzle, candidates remaining: {n}/729")
    #     solving = True
    #     while solving:
    #         solving = self.solver.solve_once(self.board)
    #         for c in self.board:
    #             if c.x == 6 and c.y == 2:
    #                 print(c.candidates)
    #             if len(c.candidates) == 0:
    #                 solving = False
    #             if len(c.candidates) == 1:
    #                 for c_m in self.board_master:
    #                     if c.x == c_m.x and c.y == c_m.y:
    #                         if c.candidates != c_m.candidates:
    #                             solving = False
    
    def test_blank_init(self):
        self.solver.solve(self.board)
        self.assertEqual(sum([len(c.candidates) for c in self.board]), 81)
        for c in self.board:
            self.assertEqual(len(c.candidates), 1)
            for c_m in self.board_master:
                if c.x == c_m.x and c.y == c_m.y:
                    self.assertEqual(c.candidates, c_m.candidates)
