from .rule import Rule
from core.update import Update
from core.cell import Cell
from core.coordinates import Coordinates
from core.utils import english_list

class PointingLines(Rule):
    rule_name = "Pointing Lines"
    as_score = 20
    cg_score = 10

    # An extension of pointing pairs
    # Instead of two paired cells pointing across the line
    # two boxes on the same line can form a pair
    # which points to the third box and eliminates
    # the values along that line in that third box

    # Variation 1:
    # Consider lines A/B/C (rows or columns) and corresponding boxes 1/2/3
    # If a value cannot be placed twice in the lines B/C of boxes 1/2
    # without those values seeing each other,
    # Then line A of boxes 1/2 form a pointing line,
    # eliminating that value in line A of box 3
    
    # This variation is demostrated in the puzzle
    # Happy Birthday Keystone by Wyrm & Rangsk
    # As published on crackingthecryptic.com/

    # To find the pointing lines, for each value
    # All possible variations for A/B/C and 1/2/3 are iterated through
    def find_update(self, board):
        for v in range(1,10):
            for b in range(3):
                for i in range(9):
                    update = self.check_col(board, v, b, i)
                    if update:
                        return update
                for j in range(9):
                    update = self.check_row(board, v, b, j)
                    if update:
                        return update
        return Update(self.rule_name)

    def check_col(self, board, v, b, i):
        boxes = [(i // 3, j) for j in range(3)]
        cells = self.cells_to_check_col(board, v, b, i)
        for k, c0 in enumerate(cells):
            for c1 in cells[k+1:]:
                if v in c0.candidates and v in c1.candidates and not self.cells_can_see(board, c0, c1):
                    return  # legal position found, not pointing line
        return self.make_update_col(board, v, b, i)
    
    def cells_to_check_col(self, board, v, b, i):
        cells = []
        for c in board:
            if c.x // 3 == i // 3 and c.x != i and c.y // 3 != b:
                cells.append(c)
        return cells

    def make_update_col(self, board, v, b, i):
        eliminations = []
        for c in board:
            if c.x == i and c.y // 3 == b and v in c.candidates:
                eliminations.append(Cell(c.x, c.y, [v]))
        return Update(self.rule_name, self.get_explanation_col(board, v, b, i), eliminations)

    def get_explanation_col(self, board, v, b, i):
        boxes = [(i // 3, j) for j in range(3) if j != b]
        box0 = boxes[0]
        box1 = boxes[1]
        col = Coordinates.int_to_col(i)
        explanation_str = f"{v} cannot be placed both in box {box0} and box {box1} without using column {col}"
        return f"For column {col}, {v} must be in box {box0} or box {box1}, because {explanation_str}."

    def check_row(self, board, v, b, j):
        boxes = [(i, j // 3) for i in range(3)]
        cells = self.cells_to_check_row(board, v, b, j)
        for k, c0 in enumerate(cells):
            for c1 in cells[k+1:]:
                if v in c0.candidates and v in c1.candidates and not self.cells_can_see(board, c0, c1):
                    return  # legal position found, not pointing line
        return self.make_update_row(board, v, b, j)
    
    def cells_to_check_row(self, board, v, b, j):
        cells = []
        for c in board:
            if c.x // 3 != b and c.y // 3 == j // 3 and c.y != j:
                cells.append(c)
        return cells

    def make_update_row(self, board, v, b, j):
        eliminations = []
        for c in board:
            if c.x // 3 == b and c.y == j and v in c.candidates:
                eliminations.append(Cell(c.x, c.y, [v]))
        return Update(self.rule_name, self.get_explanation_row(board, v, b, j), eliminations)

    def cells_can_see(self, board, c0, c1):
        if c0.x == c1.x and c0.y == c1.y:
            return False  # being the same cell doesn't count
        if (c0.x == c1.x or
            c0.y == c1.y or
            (c0.x // 3 == c1.x // 3 and c0.y // 3 == c1.y // 3)):
            return True
        for cage in board.cages:
            if c0 in cage and c1 in cage:
                return True
        return False

    def get_explanation_row(self, board, v, b, j):
        boxes = [(i, j // 3) for i in range(3) if i != b]
        box0 = boxes[0]
        box1 = boxes[1]
        row = Coordinates.int_to_row(j)
        explanation_str = f"{v} cannot be placed both in box {box0} and box {box1} without using row {row}"
        return f"For row {row}, {v} must be in box {box0} or box {box1}, because {explanation_str}."