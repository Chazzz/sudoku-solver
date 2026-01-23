from .rule import Rule
from core.update import Update
from core.cell import Cell

class BoxReduction(Rule):
    rule_name = "Box Reduction"

    # for each row/column
    # for each number
    # if candidates for that number exist in only one box
    # eliminate that number as a candidate in that box outside that row/column
    def find_update(self, board):
        for check in (self.check_rows, self.check_cols):
            update = check(board)
            if update:
                return update
        return Update(self.rule_name)

    def check_rows(self, board):
        for row in range(9):
            update = self.check_row(row, board)
            if update:
                return update

    def check_row(self, row, board):
        for i in range(1, 10):
            update = self.check_value_in_row(i, row, board)
            if update:
                return update       

    def check_value_in_row(self, value, row, board):
        cell_candidates = []
        for c in board:
            if c.y == row and value in c.candidates:
                cell_candidates.append(c)
        boxes = set([(c.x // 3, c.y // 3) for c in cell_candidates])
        if len(boxes) != 1:
            return None
        box = list(boxes)[0]
        eliminations = []
        for c in board:
            if c.x // 3 == box[0] and c.y // 3 == box[1] and c.y != row:
                if value in c.candidates:
                    eliminations.append(Cell(c.x, c.y, [value]))
        if eliminations:
            return Update(self.rule_name, self.get_row_explanation(box, row, value), eliminations)

    def get_row_explanation(self, box, row, value):
        row_str = Cell.int_to_row(row)
        return f"Row {row_str} can only be {value} inside box {box}, so no other cells in that box can be that value."

    def check_cols(self, board):
        for col in range(9):
            update = self.check_col(col, board)
            if update:
                return update

    def check_col(self, col, board):
        for i in range(1, 10):
            update = self.check_value_in_col(i, col, board)
            if update:
                return update       
    
    def check_value_in_col(self, value, col, board):
        cell_candidates = []
        for c in board:
            if c.x == col and value in c.candidates:
                cell_candidates.append(c)
        boxes = set([(c.x // 3, c.y // 3) for c in cell_candidates])
        if len(boxes) != 1:
            return None
        box = list(boxes)[0]
        eliminations = []
        for c in board:
            if c.x // 3 == box[0] and c.y // 3 == box[1] and c.x != col:
                if value in c.candidates:
                    eliminations.append(Cell(c.x, c.y, [value]))
        if eliminations:
            return Update(self.rule_name, self.get_col_explanation(box, col, value), eliminations)

    def get_col_explanation(self, box, col, value):
        col_str = Cell.int_to_col(col)
        return f"Column {col_str} can only be {value} inside box {box}, so no other cells in that box can be that value."
