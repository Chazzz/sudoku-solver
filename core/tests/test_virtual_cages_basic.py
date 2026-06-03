import unittest
from core.rules.virtual_cages_basic import VirtualCagesBasic
from core.board import Board
from core.cage import Cage
from core.coordinates import Coordinates

class TestEasyCombinations(unittest.TestCase):

    puzzle_all_cages = """
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
    
    """Missing {
            "coordinates": [
                {
                "x": 1,
                "y": 5
                }
            ],
            "sum": 9
            }
    """
    puzzle_minus_one = """
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
                "x": 4,
                "y": 4
                }
            ],
            "sum": 9
            }
        ]
        }"""
    
    """Missing {
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
                "x": 8,
                "y": 2
                },
                {
                "x": 7,
                "y": 2
                }
            ],
            "sum": 9
            }
    """
    puzzle_minus_two = """
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
                "x": 4,
                "y": 4
                }
            ],
            "sum": 9
            }
        ]
        }"""
    
    def setUp(self):
        self.board = Board()
        self.rule = VirtualCagesBasic()

    def test_one_cell_uncaged(self):
        self.board.load_json(self.puzzle_minus_one)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.virtual_cages), 1)
        self.assertEqual(len(update.virtual_cages[0].coordinates), 1)
        self.assertEqual(update.virtual_cages[0].sum, 9)
        for c in update.virtual_cages[0].coordinates:
            self.assertTrue(str(c) in ["B6"])
        self.assertEqual(update.rule_name, "Virtual Cage Creation (Basic)")
        self.assertEqual(update.explanation, "Coordinates ['B6'] are unbound in any cages. Creating virtual cage with sum 9 to contain them.")

    def test_multiple_cells_uncaged(self):
        self.board.load_json(self.puzzle_minus_two)
        update = self.rule.find_update(self.board)
        self.assertEqual(len(update.virtual_cages), 1)
        self.assertEqual(len(update.virtual_cages[0].coordinates), 3)
        self.assertEqual(update.virtual_cages[0].sum, 18)
        for c in update.virtual_cages[0].coordinates:
            self.assertTrue(str(c) in ["B6", "H3", "I3"])
        self.assertEqual(update.rule_name, "Virtual Cage Creation (Basic)")
        self.assertEqual(update.explanation, "Coordinates ['B6', 'H3', 'I3'] are unbound in any cages. Creating virtual cage with sum 18 to contain them.")

    
    def test_no_uncaged(self):
        self.board.load_json(self.puzzle_all_cages)
        update = self.rule.find_update(self.board)
        self.assertIsNone(update.virtual_cages)

    def test_no_cages(self):
        self.board.load_json(self.puzzle_all_cages)
        self.board.cages = []
        update = self.rule.find_update(self.board)
        self.assertIsNone(update.virtual_cages)

    def test_virtual_cage_existing(self):
        self.board.load_json(self.puzzle_minus_two)
        # Note: doesn't have to be correct, just not empty
        self.board.virtual_cages = [Cage([Coordinates(0,0)], 1)]
        update = self.rule.find_update(self.board)
        self.assertIsNone(update.virtual_cages)