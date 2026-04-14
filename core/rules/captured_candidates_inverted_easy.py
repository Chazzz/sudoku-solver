from .rule import Rule
from core.coordinates import Coordinates
from core.cell import Cell
from core.update import Update
from core.utils import cell_combos, english_list

class CapturedCandidatesInvertedEasy(Rule):
    rule_name = "Killer Captured Candidates 2 (Easy)"
    as_score = 20
    cg_score = 25

    # This is basically "hidden cage combinations"
    # (compare to hidden singles/doubles/triples)
    # If a row/column/box locks candidate(s) into a single cage
    # Eliminate all candidates which can't be in the cage with locked candidate(s)

    # In addition, it uses the easy combinations algorithm properties
    # Where as long as the number is in the cage that's good enough
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
            update = self.check_unit(board, unit_cells, "row")
            if update:
                return update
    
    def check_cols(self, board):
        for i in range(9):
            unit_cells = []
            for c in board:
                if c.x == i:
                    unit_cells.append(c)
            update = self.check_unit(board, unit_cells, "column")
            if update:
                return update
    
    def check_boxes(self, board):
        for i in range(9):
            unit_cells = []
            for c in board:
                if c.x // 3 == i % 3 and c.y // 3 == i // 3:
                    unit_cells.append(c)
            update = self.check_unit(board, unit_cells, "box")
            if update:
                return update
    
    def check_unit(self, board, cells, unit_name):
        # get all cages which contain 2+ cells in unit
        # iterate values 1-9
        # if value is in only one cage and in multiple cells in cage
        # mark cage as "capturing" value
        # then for all cages with captured values
        # run hard combinations with captured constraints to find any eliminations
        cages = []
        for cage in board.cages:
            times_seen = 0
            for c in cells:
                if Coordinates(c.x, c.y) in cage.coordinates:
                    times_seen += 1
                    if times_seen == 2:
                        cages.append(cage)

        for cage in cages:
            captured = []
            captured_cells = [c for c in cells if c in cage]
            for v in range(1, 10):
                in_cage_count = 0
                out_cage_count = 0
                for c in cells:
                    if v in c.candidates:
                        if c in cage:
                            in_cage_count += 1
                        else:
                            out_cage_count += 1
                if in_cage_count > 1 and out_cage_count == 0:
                    captured.append(v)
            update = self.check_cage_easy(board, cage, captured, captured_cells, unit_name)
            if update:
                return update
    
    def check_cage_easy(self, board, cage, captured, captured_cells, unit_name):
        singles = [v for v in captured]
        for c in board:
            if Coordinates(c.x, c.y) in cage.coordinates:
                if len(c.candidates) == 1:
                    singles.append(c.candidates[0])
        key = (len(cage.coordinates), cage.sum)
        combos = cell_combos[key]
        valid_values_set = set()
        for combo in combos:
            if not all(v in combo for v in singles):
                continue
            for v in combo:
                valid_values_set.add(v)
        valid_values = sorted(valid_values_set)
        eliminations = []
        for c in board:
            c_coord = Coordinates(c.x, c.y)
            if c_coord in cage.coordinates:
                eliminated_values = [v for v in c.candidates if v not in valid_values]
                if eliminated_values:
                    eliminations.append(Cell(c.x, c.y, eliminated_values))
        if eliminations:
            return Update(self.rule_name, self.get_explanation(captured, captured_cells, unit_name, cage, eliminations), eliminations)

    def make_eliminations(self, cells, possible_masks):
        eliminations = []
        for i in range(len(cells)):
            cell = cells[i]
            mask = possible_masks[i]
            unused = [v for v in cell.candidates if (mask & (1 << (v - 1))) == 0]
            if unused:
                eliminations.append(Cell(cell.x, cell.y, unused))

        # Make elimination ordering more human-readable
        eliminations.sort(key=lambda x: (x.x, x.y, x.candidates[0]))
        return eliminations

    def get_explanation(self, captured, captured_cells, unit_name, cage, eliminations):
        is_are = "is" if len(captured) == 1 else "are" 
        s1 = f"Given {english_list(captured)} {is_are} only possible in {english_list(captured_cells)} for all cells in that {unit_name}, {english_list(captured)} must be in cage {cage}."

        unpacked = [Cell(c.x, c.y, [v]) for c in eliminations for v in c.candidates]
        unpacked_s = [f"{c.candidates[0]} at {str(c)}" for c in unpacked]
        value_word = "Value" if len(unpacked) == 1 else "Values"
        return f"{s1} With that requirement, the following values are never used to form a valid sum in cage {cage}: {english_list(unpacked_s)}."

        
