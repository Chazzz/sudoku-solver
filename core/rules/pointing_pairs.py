from .rule import Rule
from core.update import Update
from core.cell import Cell

class PointingPairs(Rule):
    rule_name = "Pointing Pairs"
    as_score = 20
    cg_score = 1

    # for each box
    # for each number
    # if candidates for that number exist in only one row/column
    # eliminate that number as a candidate in that row/column outside that box
    def find_update(self, board):
        for x in range(3):
            for y in range(3):
                update = self.check_box(board, x, y)
                if update:
                    return update
        return Update(self.rule_name)

    def check_box(self, board, b_x, b_y):
        for i in range(1, 10):
            cell_candidates = []
            for c in board:
                if c.x // 3 == b_x and c.y // 3 == b_y:
                    if i in c.candidates:
                        cell_candidates.append(c)
            if len(cell_candidates) == 1:
                continue # just pairs and triples
            xs = set([c.x for c in cell_candidates])
            if len(xs) == 1:
                x = cell_candidates[0].x
                eliminations = []
                for c in board:
                    if c.x == x and not (c.x // 3 == b_x and c.y // 3 == b_y):
                        if i in c.candidates:
                            eliminations.append(Cell(c.x, c.y, [i]))
                if eliminations:
                    return Update(self.rule_name, self.get_explanation((b_x, b_y), cell_candidates, "row", i), eliminations)
            ys = set([c.y for c in cell_candidates])
            if len(ys) == 1:
                y = cell_candidates[0].y
                eliminations = []
                for c in board:
                    if c.y == y and not (c.x // 3 == b_x and c.y // 3 == b_y):
                        if i in c.candidates:
                            eliminations.append(Cell(c.x, c.y, [i]))
                if eliminations:
                    return Update(self.rule_name, self.get_explanation((b_x, b_y), cell_candidates, "column", i), eliminations)
            

    def get_explanation(self, box, cell_candidates, direction_str, value):
        return f"Box {box} can only be {value} for cells {self.english_list(cell_candidates)}, no cell in same {direction_str} outside that box can be that value."

    def english_list(self, cells):
        if not cells:
            return ""
        elif len(cells) == 1:
            return str(cells[0])
        elif len(cells) == 2:
            return f"{cells[0]} and {cells[1]}"
        else:
            # Join all but last with comma, then "and last"
            return f"{', '.join(str(x) for x in cells[:-1])}, and {cells[-1]}"
