from .rule import Rule
from core.coordinates import Coordinates
from core.cell import Cell
from core.cage import Cage
from core.update import Update
from core.utils import cell_combos, english_list

class VirtualCagesBasic(Rule):
    rule_name = "Virtual Cage Creation (Basic)"
    as_score = 1000  # Not implemented
    cg_score = 40

    # If not all cells contained in cages,
    # Add virtual cage with remaining cells
    def find_update(self, board):
        if len(board.cages) == 0 or len(board.virtual_cages) > 0:
            return Update(self.rule_name)
        cell_count = 0
        for cage in board.cages:
            cell_count += len(cage.coordinates)
        if cell_count != 81:
            return self.make_virtual_cage(board)
        return Update(self.rule_name)

    def make_virtual_cage(self, board):
        virtual_cage = Cage()
        for x in range(9):
            for y in range(9):
                c = Coordinates(x, y)
                has_cage = False
                for cage in board.cages:
                    if c in cage.coordinates:
                        has_cage = True
                if not has_cage:
                    virtual_cage.coordinates.append(c)
        virtual_cage.sum = 405
        for cage in board.cages:
            virtual_cage.sum -= cage.sum
        return Update(
            self.rule_name,
            self.get_explanation(virtual_cage),
            virtual_cages=[virtual_cage])

    def get_explanation(self, cage):
        return f"Coordinates {[str(c) for c in cage.coordinates]} are unbound in any cages. Creating virtual cage with sum {cage.sum} to contain them."