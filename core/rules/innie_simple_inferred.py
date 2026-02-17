from .innie_simple import InnieSimple
from core.update import Update
from core.cell import Cell
from core.cage import Cage
from core.coordinates import Coordinates
from functools import cache

class InnieSimpleInferred(InnieSimple):
    rule_name = "Killer Innie (1 cell, inferred)"
    as_score = 5
    cg_score = 50

    def check_row_range(self, board, row_start, row_end):
        row_cages = []
        sc_used = False
        for cage in board.cages:
            if cage.subcages:
                sc_used = True
                for sc in cage.subcages:
                    if any(row_start <= c.y <= row_end for c in sc.coordinates):
                        row_cages.append(sc)
            else:
                if any(row_start <= c.y <= row_end for c in cage.coordinates):
                    row_cages.append(cage)
        if sc_used:
            return self.check_row_cages(board, row_start, row_end, row_cages)

    def check_col_range(self, board, col_start, col_end):
        col_cages = []
        sc_used = False
        for cage in board.cages:
            if cage.subcages:
                sc_used = True
                for sc in cage.subcages:
                    if any(col_start <= c.x <= col_end for c in sc.coordinates):
                     col_cages.append(sc)
            else:
                if any(col_start <= c.x <= col_end for c in cage.coordinates):
                    col_cages.append(cage)
        if sc_used:
            return self.check_col_cages(board, col_start, col_end, col_cages)

    def check_box_combination(self, board, boxes):
        box_cages = []
        sc_used = False
        for cage in board.cages:
            if cage.subcages:
                sc_used = True
                for sc in cage.subcages:
                    if any(self.in_boxes(c, boxes) for c in sc.coordinates):
                        box_cages.append(sc)
            else:
                if any(self.in_boxes(c, boxes) for c in cage.coordinates):
                    box_cages.append(cage)
        if sc_used:
            return self.check_box_cages(board, boxes, box_cages)