import math
from core.board import Board

class Scorer:
    calibration_board = """
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

    def __init__(self):
        self.calibration_time = None

    def not_calibrated(self):
        return self.calibration_time is None

    def update_score(self, board, update_time):
        if self.not_calibrated():
            return 0
        percent = 100 * update_time/self.calibration_time
        board.scores.append(percent)
        return percent

    def get_overall_score(self, board):
        if self.not_calibrated():
            return None
        f = sum(board.times)/self.calibration_time
        if f < 1:
            return f
        else:
            return 1 + math.log(f, 2)