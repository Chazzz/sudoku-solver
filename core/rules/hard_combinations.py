from .rule import Rule
from core.update import Update
from core.cell import Cell
from core.coordinates import Coordinates
from core.utils import english_list, cell_combos

class HardCombinations(Rule):
    rule_name = "Killer Hard Combinations"
    as_score = 10
    cg_score = 10

    # Hard combinations eliminate any candidates
    # which are not used to form a valid combination in the cage
    def find_update(self, board):
        update = self.check_cages(board)
        if update:
            return update
        return Update(self.rule_name)    

    def check_cages(self, board):
        for cage in board.cages:
            update = self.check_cage_optimized(cage, board)
            if update:
                return update

    def check_cage_optimized(self, cage, board):
        # MRV heuristic: try cells with fewest candidates first
        # This prunes the search tree faster on real Killer Sudoku boards
        cells = [c for c in board if Coordinates(c.x, c.y) in cage.coordinates]
        cells.sort(key=lambda x: len(x.candidates))
        n = len(cells)  # Precompute list length     

        # Precompute conflicts which trigger prune
        conflicts = [[] for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                conflicts[i].append(j)

        # Precompute suffix min/max sums
        suffix_min = [0] * (n + 1)
        suffix_max = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_min[i] = suffix_min[i + 1] + min(cells[i].candidates)
            suffix_max[i] = suffix_max[i + 1] + max(cells[i].candidates)

        # Bitmasks (values 1-9 -> bits 0-8)
        # Faster than Python sets for small v
        possible_masks = [0] * n

        # Pruning bad sums/combos with backtrack gives ~10x performance boost
        def backtrack(idx, curr_sum, assignment):
            if idx == n:
                if curr_sum == cage.sum:
                    for i in range(n):
                        possible_masks[i] |= (1 << (assignment[i] - 1))
                return

            # O(1) remaining-sum prune
            if curr_sum + suffix_max[idx] < cage.sum or curr_sum + suffix_min[idx] > cage.sum:
                return

            for val in cells[idx].candidates:
                # Incremental conflict check against the previous visible cells
                if any(assignment[j] == val for j in conflicts[idx]):
                    continue
                assignment[idx] = val
                backtrack(idx + 1, curr_sum + val, assignment)

        assignment = [0] * n
        backtrack(0, 0, assignment)
        eliminations = self.make_eliminations(cells, possible_masks)
        if eliminations:
            return Update(self.rule_name, self.get_explanation(cage, eliminations), eliminations)

    def make_eliminations(self, cells, possible_masks):
        eliminations = []
        for i in range(len(cells)):
            cell = cells[i]
            mask = possible_masks[i]
            unused = [v for v in cell.candidates if (mask & (1 << (v - 1))) == 0]
            if unused:
                eliminations.append(Cell(cell.x, cell.y, unused))

        # Make elimination ordering more human-readable
        eliminations.sort(key=lambda x: (x.x, x.y, x.candidates[0]))
        return eliminations
   
    def cells_can_see(self, c0, c1):
        if c0.x == c1.x and c0.y == c1.y:
            return False  # being the same cell doesn't count
        return (c0.x == c1.x or
            c0.y == c1.y or
            (c0.x // 3 == c1.x // 3 and c0.y // 3 == c1.y // 3))

    def get_explanation(self, cage, eliminations):
        unpacked = [Cell(c.x, c.y, [v]) for c in eliminations for v in c.candidates]
        unpacked_s = [f"{c.candidates[0]} at {str(c)}" for c in unpacked]
        value_word = "Value" if len(unpacked) == 1 else "Values"
        return f"The following values are never used to form a valid sum in cage {cage}: {english_list(unpacked_s)}."