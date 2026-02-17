from .rule import Rule
from core.coordinates import Coordinates
from core.cell import Cell
from core.cage import Cage
from core.update import Update
from core.utils import cell_combos, english_list

class CageSplittingBasic(Rule):
    rule_name = "Killer Cage Splitting (Basic)"
    as_score = 1000  # Not implemented
    cg_score = 1

    # If a cage has a single, split the cage into
    # the single and all other cells.
    # In future updates, cage-specific rules apply to both parts of cage.
    def find_update(self, board):
        for cage in board.cages:
            update = self.check_cage(cage, board)
            if update:
                return update
        return Update(self.rule_name)

    def check_cage(self, cage, board):
        if len(cage.subcages) == len(cage.coordinates):
            return       
        for c in board:
            if Coordinates(c.x, c.y) in cage.coordinates:
                if len(c.candidates) == 1:
                    if len(cage.subcages) == 0:
                        scs = self.split_cage(cage, c)
                        return self.make_update(cage, c, scs)
                    scs = []
                    needs_update = True
                    for sc in cage.subcages:
                        if Coordinates(c.x, c.y) in sc.coordinates:
                            if len(sc.coordinates) != 1:
                                scs += self.split_cage(sc, c)
                            else:
                                needs_update = False
                        else:
                            scs.append(sc)
                    if needs_update:
                        return self.make_update(cage, c, scs)

    def split_cage(self, cage, cell):
        single = Cage([Coordinates(cell.x, cell.y)], cell.candidates[0])
        others = []
        for c in cage.coordinates:
            if c != Coordinates(cell.x, cell.y):
                others.append(c)
        other_sum = cage.sum - single.sum
        other_cage = Cage(others, other_sum)
        return [single, other_cage]

    def make_update(self, cage, c, scs):
        new_cage = Cage(cage.coordinates, cage.sum, scs)
        return Update(self.rule_name, self.split_cage_explanation(cage, c), cages=[new_cage])

    def split_cage_explanation(self, cage, c):
        return f"Cage {cage} can be split by having {c} as a separate cage."