from .rule import Rule
from core.update import Update
from core.cell import Cell

class HiddenDoubles(Rule):
    rule_name = "Hidden Doubles"

    # consider each row, column, and box
    # If only one cell in that unit has a given candidate,
    # eliminate all other candidates for that cell.

    # implemented by "For each cell with multiple candidates,
    # setting to each would need to create at least 1 elimination
    # in each of row, col and box"
    def find_update(self, board):
        n = len(board)
        for i in range(n):
            for j in range(i+1, n):
                cell1 = board[i]
                cell2 = board[j]
                if (min(len(cell1.candidates), len(cell2.candidates)) > 1 and
                    max(len(cell1.candidates), len(cell2.candidates)) > 2):
                    is_hidden, values = self.check_hidden(board, cell1, cell2)
                    if is_hidden:
                        eliminations = []
                        for c in [cell1, cell2]:
                            eliminated_values = [v for v in c.candidates if v in values]
                            if eliminated_values:
                                eliminations.append(Cell(c.x, c.y, eliminated_values))
                        if eliminations:
                            return Update(self.rule_name, self.get_explanation(board, cell1, cell2, values), eliminations)
        return Update(self.rule_name)

    def check_hidden(self, board, cell1, cell2):
        if cell1.y == cell2.y:
            values = self.row_other_candidates(board, cell1, cell2)
            if len(values) == 7:
                return True, values
        if cell1.x == cell2.x:
            values = self.col_other_candidates(board, cell1, cell2)
            if len(values) == 7:
                return True, values
        if cell1.x // 3 == cell2.x // 3 and cell1.y // 3 == cell2.y // 3:
            values = self.box_other_candidates(board, cell1, cell2)
            if len(values) == 7:
                return True, values
        return False, []

    def row_other_candidates(self, board, cell1, cell2):
        values = set()
        for c in board:
            if c.y == cell1.y and c.x != cell1.x and c.x != cell2.x:
                values.update(c.candidates)
        return sorted(values)

    def col_other_candidates(self, board, cell1, cell2):
        values = set()
        for c in board:
            if c.x == cell1.x and c.y != cell1.y and c.y != cell2.y:
                values.update(c.candidates)
        return sorted(values)

    def box_other_candidates(self, board, cell1, cell2):
        values = set()
        for c in board:
            if c.x // 3 == cell1.x // 3 and c.y // 3 == cell1.y // 3:
                if c.loc() != cell1.loc() and c.loc() != cell2.loc():
                    values.update(c.candidates)
        return sorted(values)

    def get_explanation(self, board, cell1, cell2, values_eliminated):
        location = ""
        values_remaining = []
        if cell1.y == cell2.y:
            values = self.row_other_candidates(board, cell1, cell2)
            if len(values) == 7:
                location = "all cells in that row"
                values_remaining = [i for i in range(1,10) if i not in values]
        if cell1.x == cell2.x:
            values = self.col_other_candidates(board, cell1, cell2)
            if len(values) == 7:
                location = "all cells in that column"
                values_remaining = [i for i in range(1,10) if i not in values]
        if cell1.x // 3 == cell2.x // 3 and cell1.y // 3 == cell2.y // 3:
            values = self.box_other_candidates(board, cell1, cell2)
            if len(values) == 7:
                location = "all cells in that box"
                values_remaining = [i for i in range(1,10) if i not in values]
        v0 = values_remaining[0]
        v1 = values_remaining[1]
        return f"Given {v0} and {v1} are only possible in {cell1} and {cell2} for {location}, those cell must be {v0} and {v1}."
        