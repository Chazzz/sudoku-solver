from .rule import Rule
from core.update import Update
from core.cell import Cell

class NakedDoubles(Rule):
    rule_name = "Naked Doubles"
    as_score = 5
    cg_score = 5

    # find doubles (two cells with the same two possibilities)
    # if any other cell in same row, column, or box has that candidate,
    # add that as an elimination.
    def find_update(self, board):
        n = len(board)
        for i in range(n):
            for j in range(i+1, n):
                cell1 = board[i]
                cell2 = board[j]
                if (len(cell1.candidates) == 2 and
                    cell1.candidates == cell2.candidates):
                    eliminations = self.get_eliminations(board, cell1, cell2)
                    if eliminations:
                        return Update(self.rule_name, self.get_explanation(cell1, cell2), eliminations)
        return Update(self.rule_name)
    
    def get_eliminations(self, board, cell1, cell2):
        eliminations = []
        eliminations += self.get_row_eliminations(board, cell1, cell2)
        eliminations += self.get_col_eliminations(board, cell1, cell2)
        eliminations += self.get_box_eliminations(board, cell1, cell2)
        return self.dedupe_eliminations(eliminations)

    def get_row_eliminations(self, board, cell1, cell2):
        eliminations = []
        if cell1.y != cell2.y:
            return []
        for value in cell1.candidates:
            for c in board:
                if c.y == cell1.y and c.x != cell1.x and c.x != cell2.x:
                    if value in c.candidates:
                        eliminations.append(Cell(c.x, c.y, [value]))
        return eliminations

    def get_col_eliminations(self, board, cell1, cell2):
        eliminations = []
        if cell1.x != cell2.x:
            return []
        for value in cell1.candidates:
            for c in board:
                if c.x == cell1.x and c.y != cell1.y and c.y != cell2.y:
                    if value in c.candidates:
                        eliminations.append(Cell(c.x, c.y, [value]))
        return eliminations

    def get_box_eliminations(self, board, cell1, cell2):
        eliminations = []
        if not (cell1.x // 3 == cell2.x // 3 and cell1.y // 3 == cell2.y // 3):
            return []
        for value in cell1.candidates:
            for c in board:
                if c.x // 3 == cell1.x // 3 and c.y // 3 == cell1.y // 3:
                    # Can duplicate eliminations, needs to be deduped
                    if c.loc() != cell1.loc() and c.loc() != cell2.loc():
                        if value in c.candidates:
                            eliminations.append(Cell(c.x, c.y, [value]))
        return eliminations

    def get_explanation(self, c1, c2):
        v1 = c1.candidates[0]
        v2 = c1.candidates[1]
        return f"Given {c1} and {c2} can only be {v1} and {v2}, no other cells in same row, column, or box can also be {v1} or {v2}."
        