from .rule import Rule
from core.update import Update
from core.cell import Cell
from core.coordinates import Coordinates
from core.utils import english_list, cell_combos

class EasyCombinations(Rule):
    rule_name = "Killer Easy Combinations"
    as_score = 5
    cg_score = 5

    # Easy combinations are two things:
    # 1: Obvious based on empty cage (eg. 17 size 2)
    # 2: Obvious based on partially filled in cage (eg. 21 with 6)
    # Importantly, apart from singles, don't look at cage candidates.
    def find_update(self, board):
        for check in (self.check_empty_cages, self.check_cages_with_singles):
            update = check(board)
            if update:
                return update
        return Update(self.rule_name)    

    def check_empty_cages(self, board):
        for cage in board.cages:
            update = self.check_empty_cage(cage, board)
            if update:
                return update

    def check_empty_cage(self, cage, board):    
        key = (len(cage.coordinates), cage.sum)
        combos = cell_combos[key]
        valid_values_set = set()
        for combo in combos:
            for v in combo:
                valid_values_set.add(v)
        valid_values = sorted(valid_values_set)
        eliminations = []
        for c in board:
            if Coordinates(c.x, c.y) in cage.coordinates:
                eliminated_values = [v for v in c.candidates if v not in valid_values]
                if eliminated_values:
                    eliminations.append(Cell(c.x, c.y, eliminated_values))
        if eliminations:
            return Update(self.rule_name, self.empty_cage_explanation(cage, valid_values), eliminations)

    def empty_cage_explanation(self, cage, valid_values):
        return f"Cage {cage} can only be completed using values {english_list(valid_values)}."

    def check_cages_with_singles(self, board):
        for cage in board.cages:
            update = self.check_cage_with_singles(cage, board)
            if update:
                return update
    
    def check_cage_with_singles(self, cage, board):
        singles = []
        single_coordinates = []
        for c in board:
            if Coordinates(c.x, c.y) in cage.coordinates:
                if len(c.candidates) == 1:
                    singles.append(c.candidates[0])
                    single_coordinates.append(Coordinates(c.x, c.y))
        if len(single_coordinates) == len(cage.coordinates):
            return
        key = (len(cage.coordinates) - len(singles), cage.sum - sum(singles))
        combos = cell_combos[key]
        valid_values_set = set()
        for combo in combos:
            if any(v in singles for v in combo):
                continue
            for v in combo:
                valid_values_set.add(v)
        valid_values = sorted(valid_values_set)
        eliminations = []
        for c in board:
            c_coord = Coordinates(c.x, c.y)
            if c_coord in cage.coordinates and c_coord not in single_coordinates:
                eliminated_values = [v for v in c.candidates if v not in valid_values]
                if eliminated_values:
                    eliminations.append(Cell(c.x, c.y, eliminated_values))
        if eliminations:
            return Update(self.rule_name, self.cage_with_singles_explanation(cage, singles, single_coordinates, valid_values), eliminations)

    def cage_with_singles_explanation(self, cage, singles, single_coordinates, valid_values):
        coord_str = [str(c) for c in single_coordinates]
        return f"Cage {cage} with values {singles} at {coord_str} can only be completed using values {english_list(valid_values)}."

