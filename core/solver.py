from core.rules.rule import Rule
from core.scorer import Scorer
from core.board import Board
import core.rules
import pkgutil
import importlib
import inspect
import time
import statistics

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

        rules = self.get_rules_recursive(Rule)
        self.rules = sorted([cls() for cls in rules], key=lambda x: x.cg_score)
        self.calibration_time = None
        self.scorer = Scorer()
        return
    
    def get_rules_recursive(self, subclass):
        l = [subclass]
        for s in subclass.__subclasses__():
            l += self.get_rules_recursive(s)
        return l

    def calibrate(self, iterations=7, debug=False):
        if debug:
            print("Calibrating (takes several seconds)")
        times = []
        for i in range(iterations):
            board = Board()
            board.load_json(self.scorer.calibration_board)
            self.solve(board, calibration=True)
            times.append(sum(board.times))
        self.scorer.calibration_time = statistics.median(times)
        if debug:
            print("Finished calibrating")

    def solve(self, board, debug=False, calibration=False):
        if not calibration and self.scorer.not_calibrated():
            self.calibrate(debug=debug)
        n = sum([len(c.candidates) for c in board])
        if debug:
            print(f"Solving puzzle, candidates remaining: {n}/729")
        solving = True
        while solving:
            solving = self.solve_once(board, debug, calibration)
            if self.is_completed(board):
                solving = False

            # Extra debugging tools
            # if self.wrong_solution(board):
            #     break
            # import json
            # print(json.dumps(board.cells, default=lambda o: o.__dict__))
        if self.is_completed(board):
            if debug:
                print(board.candidates_grid_string())
                print("solved puzzle")
                print(f"Grade: {self.scorer.get_overall_score(board):.2f}")
        else:
            if debug:
                n = sum([len(c.candidates) for c in board])
                print(board.candidates_grid_string())
                print(f"Unsolved puzzle, candidates remaining: {n}/729")

    def solve_once(self, board, debug=False, calibration=False):
        update = None
        t0 = time.process_time()
        for rule in self.rules:
            update = rule.find_update_with_score(board)
            if update and (update.eliminations or update.cages or update.virtual_cages):
                t1 = time.process_time()
                break
        if update and update.eliminations:
            board.times.append(t1 - t0)
            score = None
            if not calibration:
                score = self.scorer.update_score(board, t1 - t0)
            if debug:
                print(board.candidates_grid_string())
                print(update.rule_name, update.explanation, [(e, e.candidates) for e in update.eliminations])
                print(f"Score: {score:.2f}")
            self.apply_eliminations(board, update)
            return True
        if update and update.cages:
            board.times.append(t1 - t0)
            score = None
            if not calibration:
                score = self.scorer.update_score(board, t1 - t0)
            if debug:
                print(board.candidates_grid_string())
                print(update.rule_name, update.explanation, [(str(c), [str(sc) for sc in c.subcages]) for c in update.cages])
                print(f"Score: {score:.2f}")
            self.apply_cages(board, update.cages)
            return True
        if update and update.virtual_cages:
            board.times.append(t1 - t0)
            score = None
            if not calibration:
                score = self.scorer.update_score(board, t1 - t0)
            if debug:
                print(board.candidates_grid_string())
                print(update.rule_name, update.explanation, [(str(c), [str(sc) for sc in c.subcages]) for c in update.virtual_cages])
                print(f"Score: {score:.2f}")
            self.apply_virtual_cages(board, update.virtual_cages)
            return True
        return False

    def apply_eliminations(self, board, update):
        for elimination in update.eliminations:
            for c in board:
                if c.x == elimination.x and c.y == elimination.y:
                    c.candidates = [i for i in c.candidates
                        if i not in elimination.candidates]
    
    def apply_cages(self, board, cages):
        for cage in cages:
            for c in board.cages:
                if cage in c:
                    c.subcages = cage.subcages
    
    def apply_virtual_cages(self, board, virtual_cages):
        for cage in virtual_cages:
            cage_found = False
            for c in board.virtual_cages:
                if cage in c:
                    cage_found = True
                    c.subcages = cage.subcages
            if not cage_found:
                board.virtual_cages.append(cage)
    
    def is_completed(self, board):
        for c in board:
            if len(c.candidates) > 1:
                return False
        return True

    debug_soln = """
        {
        "cages": [],
        "cells": [
            {
            "x": 0,
            "y": 0,
            "candidates": [
                7
            ]
            fill in rest of puzzle...
        ]
        }"""

    def wrong_solution(self, board):
        from core.board import Board
        solution = Board()
        solution.load_json(self.debug_soln)
        for c in board:
            for sc in solution:
                if c.x == sc.x and c.y == sc.y:
                    if sc.candidates[0] not in c.candidates:
                        return True
        return False
