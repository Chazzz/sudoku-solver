from .rule import Rule
from core.update import Update
from core.cell import Cell

class NakedSinglesX(Rule):
    rule_name = "Naked Singles X"
    as_score = 1
    cg_score = 1

    # find single in X diagonal
    # if any cell in same diagonal has that candidate, add that as an elimination.
    def find_update(self, board):
        if not board.is_x:
            return Update(self.rule_name)
        for c in board:
            if c.x == c.y or c.x + c.y == 8:
                if len(c.candidates) == 1:
                    eliminations = self.get_eliminations(board, c)
                    if eliminations:
                        return Update(self.rule_name, self.get_explanation(c), eliminations)
        return Update(self.rule_name)
    
    def get_eliminations(self, board, single_cell):
        eliminations = []
        eliminations += self.get_eq_eliminations(board, single_cell)
        eliminations += self.get_plus_eliminations(board, single_cell)
        return eliminations

    def get_eq_eliminations(self, board, single_cell):
        if single_cell.x != single_cell.y:
            return []
        eliminations = []
        value = single_cell.candidates[0]
        for c in board:
            if c.x == c.y and c.y != single_cell.y and c.x != single_cell.x:
                if value in c.candidates:
                    eliminations.append(Cell(c.x, c.y, [value]))
        return eliminations

    def get_plus_eliminations(self, board, single_cell):
        if single_cell.x + single_cell.y != 8:
            return []
        eliminations = []
        value = single_cell.candidates[0]
        for c in board:
            if c.x + c.y == 8 and c.x != single_cell.x and c.y != single_cell.y:
                if value in c.candidates:
                    eliminations.append(Cell(c.x, c.y, [value]))
        return eliminations

    def get_explanation(self, c):
        value = c.candidates[0]
        return f"Given {c} can only be {value}, no cell in same diagonal can also be {value}."
        