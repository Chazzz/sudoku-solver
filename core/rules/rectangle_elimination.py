from core.board import Board
from core.update import Update
from .rule import Rule
from core.cell import Cell
from core.coordinates import Coordinates

class RectangleElimination(Rule):
    rule_name = "Rectangle Elimination"
    as_score = 25
    cg_score = 15
    
    # If only 2 possible cells for a value in a row,
    # Then eliminating value in one cell sets the other cell
    # Consider each cell as a hinge and non-hinge, alternating
    # If another cell in the same column as the hinge with value as candidate,
    # Which in combo with non-hinge cell eliminates all candidates in a box,
    # Eliminate that cell
    # And vice versa for columns vs row
    def find_update(self, board):
        for check in (self.check_rows, self.check_cols):
            update = check(board)
            if update:
                return update
        return Update(self.rule_name)
        
    def check_rows(self, board):
        for v in range(1,10):
            for y in range(9):
                cells = []
                for c in board:
                    if c.y == y and v in c.candidates:
                        cells.append(c)
                if len(cells) == 2:
                    update = self.check_row_pair(board, cells, v)
                    if update:
                        return update

    def check_row_pair(self, board, cells, value):
        eliminations = self.get_row_eliminations(board, cells[0], cells[1], value)
        if eliminations:
            return Update(self.rule_name, self.get_row_explanation(cells[0], cells[1], value), eliminations)
        eliminations = self.get_row_eliminations(board, cells[1], cells[0], value)
        if eliminations:
            return Update(self.rule_name, self.get_row_explanation(cells[1], cells[0], value), eliminations)

    def get_row_eliminations(self, board, hinge, non_hinge, value):
        for c in board:
            if c.x == hinge.x and c.y != hinge.y and value in c.candidates:
                if not self.legal_arrangement(board, c, non_hinge, value):
                    return [Cell(c.x, c.y, [value])]

    def legal_arrangement(self, board, c1, c2, value):
        for bx in range(3):
            for by in range(3):
                if not self.legal_box(board, bx, by, c1, c2, value):
                    return False
        return True

    def legal_box(self, board, bx, by, c1, c2, value):
        if c1.x // 3 == bx and c1.y // 3 == by:
            return True
        if c2.x // 3 == bx and c2.y // 3 == by:
            return True
        for c in board:
            if c.x // 3 == bx and c.y // 3 == by:
                if value in c.candidates:
                    if not self.cells_can_see(c, c1):
                        if not self.cells_can_see(c, c2):
                            return True
        return False

    def cells_can_see(self, c0, c1):
        if c0.x == c1.x and c0.y == c1.y:
            return False  # being the same cell doesn't count
        return (c0.x == c1.x or
            c0.y == c1.y or
            (c0.x // 3 == c1.x // 3 and c0.y // 3 == c1.y // 3))

    def get_row_explanation(self, hinge, non_hinge, value):
        row = Coordinates.int_to_row(hinge.y)
        return f"Row {row} can only place {value} in cells {hinge} and {non_hinge}. Therefore any cell in the same column as {hinge} cannot eliminate all candidates in a box with conjunction with {non_hinge}."
        
    def check_cols(self, board):
        for v in range(1,10):
            for x in range(9):
                cells = []
                for c in board:
                    if c.x == x and v in c.candidates:
                        cells.append(c)
                if len(cells) == 2:
                    update = self.check_col_pair(board, cells, v)
                    if update:
                        return update

    def check_col_pair(self, board, cells, value):
        eliminations = self.get_col_eliminations(board, cells[0], cells[1], value)
        if eliminations:
            return Update(self.rule_name, self.get_col_explanation(cells[0], cells[1], value), eliminations)
        eliminations = self.get_col_eliminations(board, cells[1], cells[0], value)
        if eliminations:
            return Update(self.rule_name, self.get_col_explanation(cells[1], cells[0], value), eliminations)

    def get_col_eliminations(self, board, hinge, non_hinge, value):
        for c in board:
            if c.y == hinge.y and c.x != hinge.x and value in c.candidates:
                if not self.legal_arrangement(board, c, non_hinge, value):
                    print(str(c), c.candidates)
                    return [Cell(c.x, c.y, [value])]

    def get_col_explanation(self, hinge, non_hinge, value):
        col = Coordinates.int_to_col(hinge.x)
        return f"Col {col} can only place {value} in cells {hinge} and {non_hinge}. Therefore any cell in the same row as {hinge} cannot eliminate all candidates in a box with conjunction with {non_hinge}."