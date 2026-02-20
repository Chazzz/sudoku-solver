from .hard_combinations import HardCombinations 
from core.update import Update
from core.cell import Cell
from core.coordinates import Coordinates
from core.utils import english_list, cell_combos

class HardCombinationsInferred(HardCombinations):
    rule_name = "Killer Hard Combinations (Inferred)"
    as_score = 10
    cg_score = 10

    # Same as hard combinations, but with inferred cages
    def find_update(self, board):
        update = self.check_inferred_cages(board)
        if update:
            return update
        return Update(self.rule_name)    

    def check_inferred_cages(self, board):
        for cage in board.cages:
            for subcage in cage.subcages:
                update = self.check_cage_optimized(subcage, board)
                if update:
                    return update

    def get_explanation(self, cage, eliminations):
        unpacked = [Cell(c.x, c.y, [v]) for c in eliminations for v in c.candidates]
        unpacked_s = [f"{c.candidates[0]} at {str(c)}" for c in unpacked]
        value_word = "Value" if len(unpacked) == 1 else "Values"
        return f"The following values are never used to form a valid sum in inferred cage {cage}: {english_list(unpacked_s)}."