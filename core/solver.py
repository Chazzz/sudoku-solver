from core.rules.rule import Rule
import core.rules
import pkgutil
import importlib
import inspect

class Solver:
    def __init__(self):
        # Debug code to generate cg scores
        # CG scores are based on lines of code as a proxy for complexity
        # result = {}
        # for m in pkgutil.iter_modules(core.rules.__path__, core.rules.__name__ + "."):
        #     mod = importlib.import_module(m.name)

        #     classes = [
        #         cls
        #         for _, cls in inspect.getmembers(mod, inspect.isclass)
        #         if cls.__module__ == mod.__name__
        #     ]

        #     if len(classes) != 1:
        #         raise AssertionError(
        #             f"{m.name} defines {len(classes)} classes; expected exactly 1"
        #         )

        #     cls = classes[0]
        #     try:
        #         source = inspect.getsource(cls)
        #     except OSError:
        #         continue

        #     result[m.name] = {
        #         "class": cls.__name__,
        #         "cg_score": cls.cg_score,
        #         "lines": len(source.splitlines()),
        #     }
        # s = sorted(result, key=lambda x: result[x]['lines'])
        # for v in s:
        #     print(result[v])

        for m in pkgutil.iter_modules(core.rules.__path__, core.rules.__name__ + "."):
            mod = importlib.import_module(m.name)

        self.rules = sorted([cls() for cls in Rule.__subclasses__()], key=lambda x: x.cg_score)
        return

    def solve(self, board, debug=False):
        n = sum([len(c.candidates) for c in board])
        if debug:
            print(f"Solving puzzle, candidates remaining: {n}/729")
        solving = True
        while solving:
            solving = self.solve_once(board, debug)
        if self.is_completed(board):
            if debug:
                print(board.candidates_grid_string())
                print("solved puzzle")
        else:
            if debug:
                n = sum([len(c.candidates) for c in board])
                print(board.candidates_grid_string())
                print(f"Unsolved puzzle, candidates remaining: {n}/729")

    def solve_once(self, board, debug=False):
        update = None
        for rule in self.rules:
            update = rule.find_update(board)
            if update.eliminations:
                break
        if update and update.eliminations:
            if debug:
                print(board.candidates_grid_string())
                print(update.rule_name, update.explanation, [(e, e.candidates) for e in update.eliminations])
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
