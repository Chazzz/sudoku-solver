from .rule import Rule
from core.update import Update
from core.cell import Cell
from core.cage import Cage
from core.coordinates import Coordinates
from core.utils import english_list
from functools import cache

class OutieSimple(Rule):
    rule_name = "Killer Outie (1 cell)"
    as_score = 5
    cg_score = 35

    # for each row, column and box
    # get all cages in that 9-group
    # for each group, if there's only 10 Coordinates, calculate the simple outie
    # for each group, if there's >10 coordinates but there's only one cage that is out
    # and that cage only has 1 coordinate in the group, calculate the simple innie.
    def find_update(self, board):
        for check in (self.check_rows, self.check_cols, self.check_boxes):
            update = check(board)
            if update:
                return update
        return Update(self.rule_name)
    
    def check_rows(self, board):
        for row_start in range(9):
            for row_end in range(row_start, 9):
                update = self.check_row_range(board, row_start, row_end)
                if update:
                    return update
        return None

    def check_row_range(self, board, row_start, row_end):
        row_cages = []
        for cage in board.all_cages():
            if any(row_start <= c.y <= row_end for c in cage.coordinates):
                row_cages.append(cage)
        return self.check_row_cages(board, row_start, row_end, row_cages)

    def check_row_cages(self, board, row_start, row_end, row_cages):
        combined_cage = Cage()
        for cage in row_cages:
            for c in cage.coordinates:
                combined_cage.coordinates.append(c)
            combined_cage.sum += cage.sum
        num_rows = 1 + row_end - row_start
        if (len(combined_cage.coordinates) != 9 * num_rows + 1):
            return None
        outie_coords = [c for c in combined_cage.coordinates if not (row_start <= c.y <= row_end)]
        if (len(outie_coords) != 1):
            return None
        row_sum = 45 * num_rows
        value = combined_cage.sum - row_sum
        for c in board:
            if Coordinates(c.x, c.y) in outie_coords:
                eliminated_values = [v for v in c.candidates if v != value]
                if not eliminated_values:
                    continue
                eliminations = [Cell(c.x, c.y, eliminated_values)]
                explanation = self.get_row_explanation(board, row_start, row_end, c, value)
                return Update(self.rule_name, explanation, eliminations)
        
    def get_row_explanation(self, board, row_start, row_end, c, value):
        x0 = Cell.int_to_row(row_start)
        x1 = Cell.int_to_row(row_end)
        num_rows = 1 + row_end - row_start
        row_sum = 45 * num_rows
        combined_cage_sum = row_sum + value
        row_text = ""
        row_sum_text = ""
        if x0 == x1:
            row_text = f"Row {x0} forms a cage which adds to {row_sum}"
            row_sum_text = f"and all cages containing the row sum to {combined_cage_sum}"
        else:
            row_text = f"Rows {x0}-{x1} form a cage which adds to {row_sum}"
            row_sum_text = f"and all cages containing the rows sum to {combined_cage_sum}"
        return f"{row_text}, {row_sum_text}, making {c}, the only outside cell, equal to {value}."


    def check_cols(self, board):
        for col_start in range(9):
            for col_end in range(col_start, 9):
                update = self.check_col_range(board, col_start, col_end)
                if update:
                    return update
        return None

    def check_col_range(self, board, col_start, col_end):
        col_cages = []
        for cage in board.all_cages():
            if any(col_start <= c.x <= col_end for c in cage.coordinates):
                col_cages.append(cage)
        return self.check_col_cages(board, col_start, col_end, col_cages)

    def check_col_cages(self, board, col_start, col_end, col_cages):
        combined_cage = Cage()
        for cage in col_cages:
            for c in cage.coordinates:
                combined_cage.coordinates.append(c)
            combined_cage.sum += cage.sum
        num_cols = 1 + col_end - col_start
        if (len(combined_cage.coordinates) != 9 * num_cols + 1):
            return None
        outie_coords = [c for c in combined_cage.coordinates if not (col_start <= c.x <= col_end)]
        if (len(outie_coords) != 1):
            return None
        col_sum = 45 * num_cols
        value = combined_cage.sum - col_sum
        for c in board:
            if Coordinates(c.x, c.y) in outie_coords:
                eliminated_values = [v for v in c.candidates if v != value]
                if not eliminated_values:
                    continue
                eliminations = [Cell(c.x, c.y, eliminated_values)]
                explanation = self.get_col_explanation(board, col_start, col_end, c, value)
                return Update(self.rule_name, explanation, eliminations)
        
    def get_col_explanation(self, board, col_start, col_end, c, value):
        y0 = Cell.int_to_col(col_start)
        y1 = Cell.int_to_col(col_end)
        num_cols = 1 + col_end - col_start
        col_sum = 45 * num_cols
        combined_cage_sum = col_sum + value
        col_text = ""
        col_sum_text = ""
        if y0 == y1:
            col_text = f"Column {y0} forms a cage which adds to {col_sum}"
            col_sum_text = f"and all cages containing the column sum to {combined_cage_sum}"
        else:
            col_text = f"Columns {y0}-{y1} form a cage which adds to {col_sum}"
            col_sum_text = f"and all cages containing the columns sum to {combined_cage_sum}"
        return f"{col_text}, {col_sum_text}, making {c}, the only outside cell, equal to {value}."

    def check_boxes(self, board):
        for i in range(1, 2 ** 9):
            boxes = []
            for j in range(9):
                if i // (2 ** j) % 2 == 1:
                    box_tuple = (j % 3, j // 3)
                    boxes.append(box_tuple)
            if self.is_contiguous_boxes(boxes):
                update = self.check_box_combination(board, boxes)
                if update:
                    return update
        return None

    @property
    @cache
    def box_neighbors(self):
        box_neighbors = {}
        for x in range(3):
            for y in range(3):
                neighbors = []
                if x + 1 < 3:
                    neighbors.append((x + 1, y))
                if x - 1 >= 0:
                    neighbors.append((x - 1, y))
                if y + 1 < 3:
                    neighbors.append((x, y + 1))
                if y - 1 >= 0:
                    neighbors.append((x, y - 1))
                box_neighbors[(x, y)] = neighbors
        return box_neighbors
        
    def is_contiguous_boxes(self, boxes):
        if len(boxes) == 1:
            return True
        for box in boxes:
            has_neighbor = any(b in self.box_neighbors[box] for b in boxes)
            if not has_neighbor:
                return False
        return True

    def in_boxes(self, c, boxes):
        return any(c.x // 3 == b[0] and c.y // 3 == b[1] for b in boxes)
    
    def check_box_combination(self, board, boxes):
        box_cages = []
        for cage in board.all_cages():
            if any(self.in_boxes(c, boxes) for c in cage.coordinates):
                box_cages.append(cage)
        return self.check_box_cages(board, boxes, box_cages)

    def check_box_cages(self, board, boxes, box_cages):
        combined_cage = Cage()
        for cage in box_cages:
            for c in cage.coordinates:
                combined_cage.coordinates.append(c)
            combined_cage.sum += cage.sum
        num_boxes = len(boxes)
        if (len(combined_cage.coordinates) != 9 * num_boxes + 1):
            return None
        outie_coords = [c for c in combined_cage.coordinates if not self.in_boxes(c, boxes)]
        if (len(outie_coords) != 1):
            return None
        box_sum = 45 * num_boxes
        value = combined_cage.sum - box_sum
        for c in board:
            if Coordinates(c.x, c.y) in outie_coords:
                eliminated_values = [v for v in c.candidates if v != value]
                if not eliminated_values:
                    continue
                eliminations = [Cell(c.x, c.y, eliminated_values)]
                explanation = self.get_box_explanation(board, boxes, c, value)
                return Update(self.rule_name, explanation, eliminations)

    def get_box_explanation(self, board, boxes, c, value):
        box_sum = 45 * len(boxes)
        combined_cage_sum = box_sum + value
        box_text = ""
        box_sum_text = ""
        if len(boxes) == 1:
            box_text = f"Box {english_list(boxes)} forms a cage which adds to {box_sum}"
            box_sum_text = f"and all cages containing the box sum to {combined_cage_sum}"
        else:
            box_text = f"Boxes {english_list(boxes)} form a cage which adds to {box_sum}"
            box_sum_text = f"and all cages containing the boxes sum to {combined_cage_sum}"
        return f"{box_text}, {box_sum_text}, making {c}, the only outside cell, equal to {value}."