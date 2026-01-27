from .rule import Rule
from core.update import Update
from core.cell import Cell

class NakedTriples(Rule):
    rule_name = "Naked Triples"
    as_score = 10
    cg_score = 10

    # consider each unit (row, column, and box)
    # If three cells in that unit have the same three candidates,
    # eliminate those candidates every other cell in that unit.
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
        triples = self.get_triples(cells)
        for triple in triples:
            eliminations = self.triple_eliminations(cells, triple)
            if eliminations:
                return Update(
                    self.rule_name,
                    self.get_explanation(triple, unit_name),
                    eliminations)

    def get_triples(self, cells):
        t = [c for c in cells if 2 <= len(c.candidates) <= 3]
        if len(t) < 3:
            return []
        triples = []
        n = len(t)
        # iterate through all 3-sized combinations of valid cells
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    triplet = [t[i], t[j], t[k]]
                    if len({v for c in triplet for v in c.candidates}) == 3:
                        triples.append(triplet)
        return triples
    
    def triple_eliminations(self, unit_cells, triple):
        eliminations = []
        values = {v for c in triple for v in c.candidates}
        for c in unit_cells:
            if c in triple:
                continue
            if not any(v in values for v in c.candidates):
                continue
            eliminations.append(
                Cell(c.x, c.y, [v for v in c.candidates if v in values]))
        return eliminations

    def get_explanation(self, cells, unit_name):
        values = sorted({v for c in cells for v in c.candidates})
        return f"Three cells {self.english_list(cells)} have the same three candidates {self.english_list(values)}, therefore no other cell in that {unit_name} can have that value."

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