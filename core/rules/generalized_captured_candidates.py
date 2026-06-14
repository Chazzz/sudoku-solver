from .rule import Rule
from core.coordinates import Coordinates
from core.cell import Cell
from core.update import Update
from core.utils import cell_combos, english_list

class GeneralizedCapturedCandidates(Rule):
    rule_name = "Generalized Captured Candidates"
    as_score = 1000 # (not implemented)
    cg_score = 25

    # If there is a value that has to be in a row/col/box/cage,
    # any cell outside that row/col/box/cage
    # which sees all cells in that row/col/box/cage with that value as a candidate
    # cannot also have that value as a candidate.
    def find_update(self, board):
        for check in (self.check_rows, self.check_cols, self.check_boxes, self.check_cages):
            update = check(board)
            if update:
                return update
        return Update(self.rule_name)

    def check_rows(self, board):
        for j in range(9):
            update = self.check_row(board, j)
            if update:
                return update

    def check_row(self, board, j):
        row = []
        for c in board:
            if c.y == j:
                row.append(c)
        return self.check_nine(board, row, "row", Coordinates.int_to_row(j))

    def check_cols(self, board):
        for i in range(9):
            update = self.check_col(board, i)
            if update:
                return update

    def check_col(self, board, i):
        col = []
        for c in board:
            if c.x == i:
                col.append(c)
        return self.check_nine(board, col, "col", Coordinates.int_to_col(i))
    
    def check_boxes(self, board):
        for i in range(3):
            for j in range(3):
                update = self.check_box(board, (i, j))
                if update:
                    return update

    def check_box(self, board, b):
        box = []
        for c in board:
            if c.x // 3 == b[0] and c.y // 3 == b[1]:
                box.append(c)
        return self.check_nine(board, box, "box", str(b))

    def check_nine(self, board, nine, unit_name, unit_str):
        for v in range(1,10):
            captured_coords = []
            for c in nine:
                if v in c.candidates:
                    captured_coords.append(c)
            eliminations = self.get_eliminations_for_captured_coords(board, v, captured_coords)
            if eliminations:
                return Update(self.rule_name, self.get_explanation(unit_name, unit_str, v, captured_coords), eliminations)

    def check_cages(self, board):
        for cage in board.cages:
            update = self.check_cage(board, cage)
            if update:
                return update
    
    def check_cage(self, board, cage):
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

        # A captured candidate might not be a candidate in all captured coords
        # which would make pointing cages/box reduction more likely
        # So instead of checking the set as a block
        # Instead check each captured candidate with its captured coords
        for v in captured_set:
            captured_coords = []
            for c in captured_cells:
                if v in c.candidates:
                    captured_coords.append(Coordinates(c.x, c.y))
            update = self.check_value_in_cage(board, cage, v, captured_coords)
            if update:
                return update
    
    def check_value_in_cage(self, board, cage, v, captured_coords):
        eliminations = self.get_eliminations_for_captured_coords(board, v, captured_coords)
        if eliminations:
            return Update(self.rule_name, self.get_explanation("cage", str(cage), v, captured_coords), eliminations)

    def get_explanation(self, unit_name, unit_str, v, captured_coords):
        return f"Given {unit_name} {unit_str}, all valid combinations place {v} in {english_list(captured_coords)}. Therefore, all other cells which can see {english_list(captured_coords)} can't have that value."

    def get_eliminations_for_captured_coords(self, board, v, captured_coords):
        eliminations = []
        for c in board:
            if all(self.cells_can_see(board, c, cc) for cc in captured_coords):
                if all(not(c.x == cc.x and c.y == cc.y) for cc in captured_coords):
                    if v in c.candidates:
                        eliminations.append(Cell(c.x, c.y, [v]))
        return eliminations

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