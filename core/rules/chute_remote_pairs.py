from core.board import Board
from core.cell import Cell
from core.update import Update
from core.utils import english_list
from .rule import Rule

class ChuteRemotePairs(Rule):
    rule_name = "Chute Remote Pairs"
    as_score = 25
    cg_score = 15
    
    # Look for matching pairs
    # For each matching pair, see if that pair has a chute
    # (not in same row/col/box but has same box row or box col)
    # Check that chute to see if either pair val can’t be in it.
    # For each val not in chute, eliminate val from overlapping “side chutes”
    # (cells that see both cells in pair).
    def find_update(self, board):
        pairs = self.get_pairs_dict(board)
        for pair in pairs:
            update = self.check_pair_list(board, pairs[pair])
            if update:
                return update
        return Update(self.rule_name)
    
    def get_pairs_dict(self, board):
        pairs = {}
        for c in board:
            if len(c.candidates) == 2:
                if tuple(c.candidates) in pairs:
                    pairs[tuple(c.candidates)].append(c)
                else:
                    pairs[tuple(c.candidates)] = [c]
        return pairs
    
    def check_pair_list(self, board, pair_list):
        for i in range(len(pair_list)):
            for j in range(i+1, len(pair_list)):
                update = self.check_pair(board, pair_list[i], pair_list[j])
                if update:
                    return update
    
    def check_pair(self, board, pair1, pair2):
        if pair1.x == pair2.x:
            return
        if pair1.y == pair2.y:
            return
        if pair1.x // 3 == pair2.x // 3 and pair1.y // 3 == pair2.y //3:
            return
        if not(pair1.x // 3 == pair2.x // 3 or pair1.y // 3 == pair2.y //3):
            return
        if pair1.x // 3 == pair2.x // 3:
            update = self.check_vertical_chute(board, pair1, pair2)
            if update:
                return update
        if pair1.y // 3 == pair2.y // 3:
            update = self.check_horizontal_chute(board, pair1, pair2)
            if update:
                return update

    def check_vertical_chute(self, board, pair1, pair2):
        chute = []
        side_chutes = []
        for c in board:
            if c.x // 3 == pair1.x // 3 and c.x not in [pair1.x, pair2.x]:
                if c.y // 3 not in [pair1.y // 3, pair2.y // 3]:
                    chute.append(c)
            if c.x // 3 == pair1.x // 3 and c.y // 3 == pair1.y // 3:
                if c.x == pair2.x:
                    side_chutes.append(c)
            if c.x // 3 == pair2.x // 3 and c.y // 3 == pair2.y // 3:
                if c.x == pair1.x:
                    side_chutes.append(c)
        for values in [pair1.candidates, list(reversed(pair1.candidates))]:
            eliminations = self.check_chute_eliminations(chute, side_chutes, values)
            if eliminations:
                return Update(
                    self.rule_name,
                    self.get_chute_explanation(pair1, pair2, chute, side_chutes, values),
                    eliminations)
    
    def check_horizontal_chute(self, board, pair1, pair2):
        chute = []
        side_chutes = []
        for c in board:
            if c.y // 3 == pair1.y // 3 and c.y not in [pair1.y, pair2.y]:
                if c.x // 3 not in [pair1.x // 3, pair2.x // 3]:
                    chute.append(c)
            if c.x // 3 == pair1.x // 3 and c.y // 3 == pair1.y // 3:
                if c.y == pair2.y:
                    side_chutes.append(c)
            if c.x // 3 == pair2.x // 3 and c.y // 3 == pair2.y // 3:
                if c.y == pair1.y:
                    side_chutes.append(c)
        for values in [pair1.candidates, list(reversed(pair1.candidates))]:
            eliminations = self.check_chute_eliminations(chute, side_chutes, values)
            if eliminations:
                return Update(
                    self.rule_name,
                    self.get_chute_explanation(pair1, pair2, chute, side_chutes, values),
                    eliminations)
        
    def check_chute_eliminations(self, chute, side_chutes, values):
        eliminations = []
        missing_chute_value = values[0]
        eliminated_value = values[1]
        for c in chute:
            if missing_chute_value in c.candidates:
                return
        for c in side_chutes:
            if eliminated_value in c.candidates:
                eliminations.append(Cell(c.x, c.y, [eliminated_value]))
        return eliminations

    def get_chute_explanation(self, pair1, pair2, chute, side_chutes, values):
        missing_chute_value = values[0]
        eliminated_value = values[1]
        pairs = (pair1, pair2)
        s1 = f"Matching pairs {english_list(sorted(values))} in cells {english_list(pairs)}"
        s2 = f" form a chute {english_list(chute)} which doesn't contain {missing_chute_value}. "
        s3 = f"Therefore, {english_list(pairs)} can't both be {missing_chute_value}. "
        s4 = f"Any {eliminated_value} in cells {english_list(side_chutes)} would force this. "
        s5 = f"Therefore, {eliminated_value} can't be in cells {english_list(side_chutes)}."
        return s1 + s2 + s3 + s4 + s5