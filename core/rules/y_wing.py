from core.board import Board
from core.update import Update
from .rule import Rule
from core.cell import Cell
from core.coordinates import Coordinates

class YWing(Rule):
    rule_name = "Y Wing"
    as_score = 50
    cg_score = 5
    
    # If there is a double AB with two "wings"
    # AC and BC that can see AB
    # No cell that can see both AC and BC can be C

    # This is implemented by finding doubles AB
    # and then finding wing 1 AC, and wing 2 BC
    # iterating through all wings to first check wings see AB
    # Then eliminating C in any cells that see both AC and BC 
    def find_update(self, board):
        doubles = self.get_doubles(board)
        for double in doubles:
            update = self.check_double(board, double)
            if update:
                return update
        return Update(self.rule_name)

    def get_doubles(self, board, value=None, wing_cell=None):
        doubles = []
        for c in board:
            if len(c.candidates) == 2:
                if not value or tuple(c.candidates) == value:
                    if not wing_cell or self.cells_can_see(c, wing_cell):
                        doubles.append(c)
        return doubles

    def check_double(self, board, double):
        v0 = double.candidates[0]
        v1 = double.candidates[1]
        for i in range(1, 10):
            wings0 = self.get_doubles(board, value=tuple(sorted((v0, i))), wing_cell=double)
            wings1 = self.get_doubles(board, value=tuple(sorted((v1, i))), wing_cell=double)
            for w0 in wings0:
                for w1 in wings1:
                    eliminations = self.get_wing_eliminations(board, w0, w1, i)
                    if eliminations:
                        return Update(self.rule_name, self.get_explanation(double, w0, w1, i), eliminations)

    def get_wing_eliminations(self, board, w0, w1, value):
        eliminations = []
        for c in board:
            if self.cells_can_see(c, w0) and self.cells_can_see(c, w1):
                if value in c.candidates:
                    eliminations.append(Cell(c.x, c.y, [value]))
        return eliminations

    def cells_can_see(self, c0, c1):
        if c0.x == c1.x and c0.y == c1.y:
            return False  # being the same cell doesn't count
        return (c0.x == c1.x or
            c0.y == c1.y or
            (c0.x // 3 == c1.x // 3 and c0.y // 3 == c1.y // 3))

    def get_explanation(self, double, w0, w1, i):
        return f"Double at {double} forms two wings with {w0} and {w1}, eliminating all candidates {i} that can see both {w0} and {w1}."