from .rule import Rule
from core.update import Update
from core.cell import Cell
from core.coordinates import Coordinates
from core.utils import english_list, cell_combos

class HardCombinations(Rule):
    rule_name = "Killer Hard Combinations"
    as_score = 10
    cg_score = 5

    # Hard combinations eliminate any candidates
    # which are not used to form a valid combination in the cage
    def find_update(self, board):
        update = self.check_cages(board)
        if update:
            return update
        return Update(self.rule_name)    

    def check_cages(self, board):
        for cage in board.cages:
            update = self.check_cage(cage, board)
            if update:
                return update

    def check_cage(self, cage, board):
        cells = []
        for c in board:
            if Coordinates(c.x, c.y) in cage.coordinates:
                cells.append(c)
        candidates_used = [set() for _ in range(len(cells))]
        for combo in self.one_of_each_iter(cells):
            if len(set(combo)) == len(combo) and sum(combo) == cage.sum:
                for i, v in enumerate(combo):
                    candidates_used[i].add(v)
        eliminations = []
        for c, used in zip(cells, candidates_used):
            unused = [v for v in c.candidates if v not in used]
            if unused:
                eliminations.append(Cell(c.x, c.y, unused))
        if eliminations:
            return Update(self.rule_name, self.get_explanation(cage, eliminations), eliminations)

    def one_of_each_iter(self, cells):
        odometer = [0 for _ in range(len(cells))]
        while True:
            yield [c.candidates[v] for c, v in zip(cells, odometer)]
            # increment leftmost index with rollover
            for i in range(len(odometer)):
                odometer[i] += 1
                if odometer[i] != len(cells[i].candidates):
                    break
                else:
                    odometer[i] = 0
            if sum(odometer) == 0:
                return  # prevent loop back to beginning

    def get_explanation(self, cage, eliminations):
        unpacked = [Cell(c.x, c.y, [v]) for c in eliminations for v in c.candidates]
        unpacked_s = [f"{c.candidates[0]} at {str(c)}" for c in unpacked]
        value_word = "Value" if len(unpacked) == 1 else "Values"
        return f"The following values are never used to form a valid sum in cage {cage}: {english_list(unpacked_s)}."