from .rule import Rule
from core.coordinates import Coordinates
from core.cell import Cell
from core.update import Update
from core.utils import cell_combos, english_list

class CapturedCandidatesDouble(Rule):
    rule_name = "Killer Captured Candidates (Double)"
    as_score = 1000 # Not implemented
    cg_score = 20

    # This is captured candidates
    # but for two cages in two adjacent rows/columns/boxes
    def find_update(self, board):
        for i, cage1 in enumerate(board.cages):
            for cage2 in board.cages[i+1:]:
                update = self.check_cage_double(board, cage1, cage2)
                if update:
                    return update
        return Update(self.rule_name)
    
    def check_cage_double(self, board, cage1, cage2):
        cells1, set1 = self.get_captured(board, cage1)
        cells2, set2 = self.get_captured(board, cage2)
        captured_cells = cells1 + cells2
        captured_set = set1 & set2
        if len(captured_set) == 0:
            return

        # After merging cages, check is virtually identical
        # Except for len(rows/cols/boxes) >= 3 instead of 2
        # And 2 cages to construct explanations with
        for v in captured_set:
            captured_coords = []
            for c in captured_cells:
                if v in c.candidates:
                    captured_coords.append(Coordinates(c.x, c.y))
            update = self.check_value_in_cages(board, cage1, cage2, v, captured_coords)
            if update:
                return update

    def get_captured(self, board, cage):
        singles = []
        single_cells = []
        captured_cells = []
        for c in board:
            if Coordinates(c.x, c.y) in cage.coordinates:
                if len(c.candidates) == 1:
                    singles.append(c.candidates[0])
                    single_cells.append(c)
                else:
                    captured_cells.append(c)
        if not captured_cells:
            return [], set()
        key = (len(cage.coordinates) - len(singles), cage.sum - sum(singles))
        combos = cell_combos[key]
        captured_set = set(range(1,10))
        for combo in combos:
            if any(v in singles for v in combo):
                continue
            captured_set &= set(combo)
        return captured_cells, captured_set 
    
    def check_value_in_cages(self, board, cage1, cage2, v, captured_coords):
        for check in (self.check_rows, self.check_cols, self.check_boxes):
            update = check(board, cage1, cage2, set([v]), captured_coords)
            if update:
                return update

    def check_rows(self, board, cage1, cage2, captured_set, captured_coords):
        rows = list(set([c.y for c in captured_coords]))
        if len(rows) >= 3:
            return
        eliminations = []
        for row in rows:
            cells_to_check = []
            for c in board:
                if c.y == row and all(not(c.x == coord.x and c.y == coord.y) for coord in captured_coords):
                    cells_to_check.append(c)
            eliminations += self.get_eliminations(captured_set, cells_to_check)
        if eliminations:
            return Update(
                self.rule_name,
                self.get_explanation(cage1, cage2, captured_set, captured_coords, "rows"),
                eliminations)
    
    def check_cols(self, board, cage1, cage2, captured_set, captured_coords):
        cols = list(set([c.x for c in captured_coords]))
        if len(cols) >= 3:
            return
        eliminations = []
        for col in cols:
            cells_to_check = []
            for c in board:
                if c.x == col and all(not(c.x == coord.x and c.y == coord.y) for coord in captured_coords):
                    cells_to_check.append(c)
            eliminations += self.get_eliminations(captured_set, cells_to_check)
        if eliminations:
            return Update(
                self.rule_name,
                self.get_explanation(cage1, cage2, captured_set, captured_coords, "columns"),
                eliminations)
        
    def check_boxes(self, board, cage1, cage2, captured_set, captured_coords):
        boxes = list(set([(c.x // 3, c.y // 3) for c in captured_coords]))
        if len(boxes) >= 3:
            return
        eliminations = []
        for box in boxes:
            cells_to_check = []
            for c in board:
                if ((c.x // 3 == box[0] and c.y // 3 == box[1]) and
                    all(not(c.x == coord.x and c.y == coord.y) for coord in captured_coords)):
                    cells_to_check.append(c)
            eliminations += self.get_eliminations(captured_set, cells_to_check)
        if eliminations:
            return Update(
                self.rule_name,
                self.get_explanation(cage1, cage2, captured_set, captured_coords, "boxes"),
                eliminations)

    def get_eliminations(self, captured_set, cells_to_check):
        eliminations = []
        for c in cells_to_check:
            eliminated_set = captured_set & set(c.candidates)
            if len(eliminated_set) >= 1:
                eliminations.append(Cell(c.x, c.y, sorted(eliminated_set)))
        return eliminations
    
    def get_explanation(self, cage1, cage2, captured_set, captured_coords, unit_name):
        values = sorted(captured_set)
        return f"Given cage {cage1} and cage {cage2}, all valid combinations place {english_list(values)} in {english_list(captured_coords)}. Therefore, all other cells in the same {unit_name} can't have that value."



        

    