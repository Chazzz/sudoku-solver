from core.board import Board
from core.update import Update
from .rule import Rule
from core.cell import Cell
from core.coordinates import Coordinates
from core.utils import english_list

class WWing(Rule):
    rule_name = "W Wing"
    as_score = 25
    cg_score = 10
    
    # If you have 3 chained mutually exclusive pairs AB (the "W")
    # Both ends can potentially see a cell which is neither A nor B
    # This is because however you chain the AB pairs,
    # Both ends of the W will be one A and one B.
    def find_update(self, board):
        for v0 in range(1, 9):
            for v1 in range(v0, 10):
                update = self.check_pair(board, v0, v1)
                if update:
                    return update
        return Update(self.rule_name)

    def check_pair(self, board, v0, v1):
        doubles = []
        for c in board:
            if c.candidates == [v0, v1]:
                doubles.append(c)
        if len(doubles) < 4:
            return
        d = self.make_chain_dict(doubles)
        # naive chaining
        for k in d:
            for k2 in d[k]:
                for k3 in d[k2]:
                    for k4 in d[k3]:
                        update = self.check_w(board, k, k2, k3, k4, v0, v1)
                        if update:
                            return update
    
    def make_chain_dict(self, doubles):
        c = {}
        for d0 in doubles:
            c[(d0.x, d0.y)] = []
            shares_row = [d1 for d1 in doubles if d0.y == d1.y and d0.x != d1.x]
            shares_col = [d1 for d1 in doubles if d0.x == d1.x and d0.y != d1.y]
            shares_box = [d1 for d1 in doubles if self.shares_box(d0, d1)]
            for s in [shares_row, shares_col, shares_box]:
                if len(s) == 1:
                    c[(d0.x, d0.y)].append((s[0].x, s[0].y))
            c[(d0.x, d0.y)] = sorted(c[(d0.x, d0.y)])  # optional
        return c

    def shares_box(self, d0, d1):
        return (
            d0.x // 3 == d1.x // 3 and
            d0.y // 3 == d1.y // 3 and
            (d0.x != d1.x and d0.y != d1.y))

    def check_w(self, board, k, k2, k3, k4, v0, v1):
        if k == k3 or k2 == k4:
            return
        e_cells = []
        for c in board:
            if ((c.x, c.y) != k2 and 
                (c.x, c.y) != k3 and 
                self.cells_can_see(c, k) and
                self.cells_can_see(c, k4)):
                eliminations = [v for v in c.candidates if v in [v0, v1]]
                if eliminations:
                    e_cells.append(Cell(c.x, c.y, eliminations))
        if e_cells:
            return Update(self.rule_name, self.get_explanation(k, k2, k3, k4, v0, v1), e_cells)


    def cells_can_see(self, c, k):
        if c.x == k[0] and c.y == k[1]:
            return False  # being the same cell doesn't count
        return (c.x == k[0] or
            c.y == k[1] or
            (c.x // 3 == k[0] // 3 and c.y // 3 == k[1] // 3))

    def get_explanation(self, k1, k2, k3, k4, v0, v1):
        c1 = Cell(k1[0], k1[1])
        c2 = Cell(k2[0], k2[1])
        c3 = Cell(k3[0], k3[1])
        c4 = Cell(k4[0], k4[1])
        return f"Mutualy exclusive pair {(v0, v1)} forms a \"W\" at {english_list([c1, c2, c3, c4])}, eliminating {v0} and {v1} for a cell which sees both {c1} and {c4}."