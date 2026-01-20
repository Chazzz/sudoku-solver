import core.rules.naked_singles
import core.rules.hidden_singles
import core.rules.naked_doubles
import core.rules.hidden_doubles
from core.rules.rule import Rule

class Solver:
    def __init__(self):
        self.rules = [cls() for cls in Rule.__subclasses__()]
        return

    def solve(self, board):
        n = sum([len(c.candidates) for c in board])
        print(f"Solving puzzle, candidates remaining: {n}/729")
        solving = True
        while solving:
            solving = self.solve_once(board)
        if self.is_completed(board):
            print("solved puzzle")
        else:
            n = sum([len(c.candidates) for c in board])
            print(f"Unsolved puzzle, candidates remaining: {n}/729")

    def solve_once(self, board):
        update = None
        for rule in self.rules:
            update = rule.find_update(board)
            if update.eliminations:
                break
        if update and update.eliminations:
            board = self.apply_eliminations(board, update)
            return True
        return False

    def apply_eliminations(self, board, update):
        for elimination in update.eliminations:
            for c in board:
                if c.x == elimination.x and c.y == elimination.y:
                    c.candidates = [i for i in c.candidates
                        if i not in elimination.candidates]
        return board
    
    def is_completed(self, board):
        for c in board:
            if len(c.candidates) != 1:
                return False
        return True
