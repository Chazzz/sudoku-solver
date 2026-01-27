from .rule import Rule
from core.update import Update
from core.cell import Cell

class NakedSingles(Rule):
    rule_name = "Naked Singles"
    as_score = 1
    cg_score = 1

    # find single
    # if any cell in same row, column, or box has that candidate, add that as an elimination.
    def find_update(self, board):
        for c in board:
            if len(c.candidates) == 1:
                eliminations = self.get_eliminations(board, c)
                if eliminations:
                    return Update(self.rule_name, self.get_explanation(c), eliminations)
        return Update(self.rule_name)
    
    def get_eliminations(self, board, single_cell):
        eliminations = []
        eliminations += self.get_row_eliminations(board, single_cell)
        eliminations += self.get_col_eliminations(board, single_cell)
        eliminations += self.get_box_eliminations(board, single_cell)
        return eliminations

    def get_row_eliminations(self, board, single_cell):
        eliminations = []
        value = single_cell.candidates[0]
        for c in board:
            if c.y == single_cell.y and c.x != single_cell.x:
                if value in c.candidates:
                    eliminations.append(Cell(c.x, c.y, [value]))
        return eliminations

    def get_col_eliminations(self, board, single_cell):
        eliminations = []
        value = single_cell.candidates[0]
        for c in board:
            if c.x == single_cell.x and c.y != single_cell.y:
                if value in c.candidates:
                    eliminations.append(Cell(c.x, c.y, [value]))
        return eliminations

    def get_box_eliminations(self, board, single_cell):
        eliminations = []
        value = single_cell.candidates[0]
        for c in board:
            if c.x // 3 == single_cell.x // 3 and c.y // 3 == single_cell.y // 3:
                # Ignore overlapping same-row and same-col eliminations
                if c.x != single_cell.x and c.y != single_cell.y:
                    if value in c.candidates:
                        eliminations.append(Cell(c.x, c.y, [value]))
        return eliminations

    def get_explanation(self, c):
        value = c.candidates[0]
        return f"Given {c} can only be {value}, no cell in same row, column, or box can also be {value}."
        