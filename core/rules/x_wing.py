from core.board import Board
from core.update import Update
from .rule import Rule
from core.cell import Cell
from core.coordinates import Coordinates

class XWing(Rule):
    rule_name = "X Wing"
    as_score = 30
    cg_score = 15
    
    # If only 2 possible columns for a value in 2 different rows,
    # And those 2 columns are the same,
    # Eliminate that value for those columns in other rows
    # And vice versa for 2 possible rows for a value in 2 different columns
    def find_update(self, board):
        for check in (self.check_rows, self.check_cols):
            update = check(board)
            if update:
                return update
        return Update(self.rule_name)
        
    def check_rows(self, board):
        for i in range(1,10):
            row_tuples = self.get_row_tuples(board, i)
            seen = set()
            dupes = []
            for t in row_tuples:
                if t in seen:
                    dupes.append(t)
                else:
                    seen.add(t)
            for d in dupes:
                eliminations = self.row_eliminations(board, d, i)
                if eliminations:
                    return Update(self.rule_name, self.get_row_explanation(d, i), eliminations)

    # for each col, the tuple of rows with value
    def get_row_tuples(self, board, value):
        tuples = []
        for x in range(9):
            ys = []
            for c in board:
                if c.x == x and value in c.candidates:
                    ys.append(c.y)
            if len(ys) == 2:
                tuples.append(tuple(ys))
        return tuples
    
    def row_eliminations(self, board, d_tuple, value):
        eliminations = []
        for x in range(9):
            ys = []
            for c in board:
                if c.x == x and value in c.candidates:
                    ys.append(c.y)
            if tuple(ys) == d_tuple:
                continue
            for c in board:
                if c.x == x and c.y in d_tuple and value in c.candidates:
                    eliminations.append(Cell(c.x, c.y, [value]))
        return eliminations

    def get_row_explanation(self, d, i):
        row0 = Coordinates.int_to_row(d[0])
        row1 = Coordinates.int_to_row(d[1])
        return f"Two columns can only place {i} in row {row0} and {row1}. Therefore no other column can place {i} in row {row0} and {row1}."
  

    def check_cols(self, board):
        for i in range(1,10):
            col_tuples = self.get_col_tuples(board, i)
            seen = set()
            dupes = []
            for t in col_tuples:
                if t in seen:
                    dupes.append(t)
                else:
                    seen.add(t)
            for d in dupes:
                eliminations = self.col_eliminations(board, d, i)
                if eliminations:
                    return Update(self.rule_name, self.get_col_explanation(d, i), eliminations)
    
    def get_col_tuples(self, board, value):
        tuples = []
        for y in range(9):
            xs = []
            for c in board:
                if c.y == y and value in c.candidates:
                    xs.append(c.x)
            if len(xs) == 2:
                tuples.append(tuple(xs))
        return tuples
    
    def col_eliminations(self, board, d_tuple, value):
        eliminations = []
        for y in range(9):
            xs = []
            for c in board:
                if c.y == y and value in c.candidates:
                    xs.append(c.x)
            if tuple(xs) == d_tuple:
                continue
            for c in board:
                if c.y == y and c.x in d_tuple and value in c.candidates:
                    eliminations.append(Cell(c.x, c.y, [value]))
        return eliminations

    def get_col_explanation(self, d, i):
        col0 = Coordinates.int_to_col(d[0])
        col1 = Coordinates.int_to_col(d[1])
        return f"Two rows can only place {i} in column {col0} and {col1}. Therefore no other row can place {i} in column {col0} and {col1}."
