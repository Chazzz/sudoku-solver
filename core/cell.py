from .coordinates import Coordinates
from functools import total_ordering

@total_ordering
class Cell(Coordinates):
    def __init__(self, x, y, candidates=None):
        super().__init__(x, y)
        if candidates:
            self.candidates = candidates
        else:
            self.candidates = list(range(1,10)) # 1-9

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__str__()

    def __eq__(self, other):
        if not isinstance(other, Cell):
            return NotImplemented
        return (
            self.x == other.x and
            self.y == other.y and
            self.candidates == other.candidates)
    
    def __lt__(self, other):
        if not isinstance(other, Cell):
            return NotImplemented
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x

    def __hash__(self):
        return super().__hash__()
    