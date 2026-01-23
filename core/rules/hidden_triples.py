from .rule import Rule
from core.update import Update
from core.cell import Cell

class HiddenTriples(Rule):
    rule_name = "Hidden Triples"

    # consider each unit (row, column, and box)
    # If three candidates can only be in three cells in that unit,
    # eliminate all other candidates for those cells.
    def find_update(self, board):
        for check in (self.check_rows, self.check_cols, self.check_boxes):
            update = check(board)
            if update:
                return update
        return Update(self.rule_name)

    def check_rows(self, board):
        for i in range(9):
            unit_cells = []
            for c in board:
                if c.y == i:
                    unit_cells.append(c)
            update = self.check_unit(unit_cells, "row")
            if update:
                return update

    def check_cols(self, board):
        for i in range(9):
            unit_cells = []
            for c in board:
                if c.x == i:
                    unit_cells.append(c)
            update = self.check_unit(unit_cells, "column")
            if update:
                return update
    
    def check_boxes(self, board):
        for i in range(9):
            unit_cells = []
            for c in board:
                if c.x // 3 == i % 3 and c.y // 3 == i // 3:
                    unit_cells.append(c)
            update = self.check_unit(unit_cells, "box")
            if update:
                return update

    def check_unit(self, cells, unit_name):
        # iterate through all 3-sized combinations of values 1-9
        # other than the values that go in too many or too few cells
        t = [v for v in range(1,10) if 2 <= len([c for c in cells if v in c.candidates]) <= 3]
        if len(t) < 3:
            return []
        triples = []
        n = len(t)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    triplet = [t[i], t[j], t[k]]
                    update = self.check_triplet(triplet, cells, unit_name)
                    if update:
                        return update

    def check_triplet(self, triplet, cells, unit_name):
        triplet_cells = sorted({c for v in triplet for c in cells if v in c.candidates})
        if len(triplet_cells) == 3:
            if (any(v for c in triplet_cells for v in c.candidates if v not in triplet)):
                eliminations = [Cell(c.x, c.y, [v for v in c.candidates if v not in triplet]) for c in triplet_cells]
                return Update(
                    self.rule_name,
                    self.get_explanation(triplet_cells, unit_name, triplet),
                    eliminations)

    def get_explanation(self, cells, unit_name, values):
        return f"Given {self.english_list(values)} are only possible in {self.english_list(cells)} for all cells in that {unit_name}, those cell must be {self.english_list(values)}."

    def english_list(self, values):
        if not values:
            return ""
        elif len(values) == 1:
            return str(values[0])
        elif len(values) == 2:
            return f"{values[0]} and {values[1]}"
        else:
            # Join all but last with comma, then "and last"
            return f"{', '.join(str(x) for x in values[:-1])}, and {values[-1]}"