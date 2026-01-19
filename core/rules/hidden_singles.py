from .rule import Rule
from core.update import Update
from core.cell import Cell

class HiddenSingles(Rule):
    rule_name = "Hidden Singles"

    # consider each row, column, and box
    # If only one cell in that unit has a given candidate,
    # eliminate all other candidates for that cell.

    # implemented by "For each cell with multiple candidates,
    # setting to each would need to create at least 1 elimination
    # in each of row, col and box"
    def find_update(self, board):
        for c in board:
            if len(c.candidates) != 1:
                for value in c.candidates:
                    is_hidden = self.check_hidden(board, c, value)
                    if is_hidden:
                        eliminations = [Cell(c.x, c.y, [v for v in c.candidates if v != value])]
                        return Update(self.rule_name, self.get_explanation(board, c, value), eliminations)
        return Update(self.rule_name)
    
    def check_hidden(self, board, single_cell, value):
        return not (
            self.has_row_eliminations(board, single_cell, value) and
            self.has_col_eliminations(board, single_cell, value) and
            self.has_box_eliminations(board, single_cell, value))

    def has_row_eliminations(self, board, single_cell, value):
        for c in board:
            if c.y == single_cell.y and c.x != single_cell.x:
                if value in c.candidates:
                    return True
        return False

    def has_col_eliminations(self, board, single_cell, value):
        for c in board:
            if c.x == single_cell.x and c.y != single_cell.y:
                if value in c.candidates:
                    return True
        return False

    def has_box_eliminations(self, board, single_cell, value):
        for c in board:
            if c.x // 3 == single_cell.x // 3 and c.y // 3 == single_cell.y // 3:
                # Consider overlapping same-row and same-col candidates
                if c.x != single_cell.x or c.y != single_cell.y:
                    if value in c.candidates:
                        return True
        return False

    def get_explanation(self, board, cell, value):
        single_in_row = not self.has_row_eliminations(board, cell, value)
        single_in_col = not self.has_col_eliminations(board, cell, value)
        single_in_box = not self.has_box_eliminations(board, cell, value)
        location = ""
        if single_in_row:
            location = "all cells in that row"
        if single_in_col:
            location = "all cells in that column"
        if single_in_box:
            location = "all cells in that box"
        return f"Given {value} is only possible in {cell} for {location}, that cell must be {value}."
        