from .rule import Rule
from core.coordinates import Coordinates
from core.cell import Cell
from core.update import Update
from core.utils import cell_combos, english_list

class CapturedCandidates(Rule):
    rule_name = "Killer Captured Candidates"

    # If a candidate has to be in a specific cage, remove it from qualified rows/columns/box
    # Cage-by-cage helps make sure that the coordinates that are captured are not already singles. 
    def find_update(self, board):
        for cage in board.cages:
            update = self.check_cage(board, cage)
            if update:
                return update
        return Update(self.rule_name)
    
    def check_cage(self, board, cage):
        singles = []
        single_coordinates = []
        captured_coords = []
        for c in board:
            if Coordinates(c.x, c.y) in cage.coordinates:
                if len(c.candidates) == 1:
                    singles.append(c.candidates[0])
                    single_coordinates.append(Coordinates(c.x, c.y))
                else:
                    captured_coords.append(Coordinates(c.x, c.y))
        if not captured_coords:
            return
        key = (len(cage.coordinates) - len(singles), cage.sum - sum(singles))
        combos = cell_combos[key]
        captured_set = set(range(1,10))
        for combo in combos:
            if any(v in singles for v in combo):
                continue
            captured_set &= set(combo)
        if len(captured_set) == 0:
            return
        for check in (self.check_rows, self.check_cols, self.check_boxes):
            update = check(board, cage, captured_set, captured_coords)
            if update:
                return update
        return Update(self.rule_name)

    def check_rows(self, board, cage, captured_set, captured_coords):
        rows = list(set([c.y for c in captured_coords]))
        if len(rows) >= 2:
            return
        row = rows[0]
        cells_to_check = []
        for c in board:
            if c.y == row and all(c.x != coord.x for coord in captured_coords):
                cells_to_check.append(c)
        eliminations = self.get_eliminations(captured_set, cells_to_check)
        if eliminations:
            return Update(
                self.rule_name,
                self.get_explanation(cage, captured_set, captured_coords, "row"),
                eliminations)
    
    def check_cols(self, board, cage, captured_set, captured_coords):
        cols = list(set([c.x for c in captured_coords]))
        if len(cols) >= 2:
            return
        col = cols[0]
        cells_to_check = []
        for c in board:
            if c.x == col and all(c.y != coord.y for coord in captured_coords):
                cells_to_check.append(c)
        eliminations = self.get_eliminations(captured_set, cells_to_check)
        if eliminations:
            return Update(
                self.rule_name,
                self.get_explanation(cage, captured_set, captured_coords, "column"),
                eliminations)
        
    def check_boxes(self, board, cage, captured_set, captured_coords):
        boxes = list(set([(c.x // 3, c.y // 3) for c in captured_coords]))
        if len(boxes) >= 2:
            return
        box = boxes[0]
        cells_to_check = []
        for c in board:
            if ((c.x // 3 == box[0] and c.y // 3 == box[1]) and
                all(not(c.x == coord.x and c.y == coord.y) for coord in captured_coords)):
                cells_to_check.append(c)
        eliminations = self.get_eliminations(captured_set, cells_to_check)
        if eliminations:
            return Update(
                self.rule_name,
                self.get_explanation(cage, captured_set, captured_coords, "box"),
                eliminations)

    def get_eliminations(self, captured_set, cells_to_check):
        eliminations = []
        for c in cells_to_check:
            eliminated_set = captured_set & set(c.candidates)
            if len(eliminated_set) >= 1:
                eliminations.append(Cell(c.x, c.y, sorted(eliminated_set)))
        return eliminations
    
    def get_explanation(self, cage, captured_set, captured_coords, unit_name):
        values = sorted(captured_set)
        return f"Given cage {cage}, all valid combinations place {english_list(values)} in {english_list(captured_coords)}. Therefore, all other cells in the same {unit_name} can't have that value."



        

    