from .rule import Rule
from core.update import Update
from core.cell import Cell
from core.coordinates import Coordinates
from core.utils import english_list, cell_combos

class HardCombinationsDouble(Rule):
    rule_name = "Double Killer Hard Combinations"
    as_score = 1000  # n/a
    cg_score = 15

    # Hard combinations eliminate any candidates
    # which are not used to form a valid combination in the cage
    def find_update(self, board):
        update = self.check_cages(board)
        if update:
            return update
        return Update(self.rule_name)    

    def check_cages(self, board):
        for i, cage1 in enumerate(board.cages):
            for cage2 in board.cages[i + 1:]:
                update = self.check_double_cage_optimized(cage1, cage2, board)
                if update:
                    return update

    def check_double_cage_optimized(self, cage1, cage2, board):
        # MRV heuristic: try cells with fewest candidates first
        # This prunes the search tree faster on real Killer Sudoku boards
        cells1 = [(c, cage1) for c in board if Coordinates(c.x, c.y) in cage1.coordinates]
        cells2 = [(c, cage2) for c in board if Coordinates(c.x, c.y) in cage2.coordinates]
        cells = cells1 + cells2
        cells.sort(key=lambda x: len(x[0].candidates))
        n = len(cells)  # Precompute list length     

        # Precompute conflicts which trigger prune
        conflicts = [[] for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if self.cells_can_see(cells[i], cells[j]):
                    conflicts[i].append(j)

        t_sum = lambda x: x * (x-1) / 2
        t_sum_2cage = t_sum(len(cage1.coordinates)) + t_sum(len(cage2.coordinates))
        if sum([len(x) for x in conflicts]) <= t_sum_2cage:
            return

        # Precompute cage_index which update sums
        cage_index = [0 if cell[1] == cage1 else 1 for cell in cells]

        # Precompute suffix min/max sums
        suffix_min = [0] * (n + 1)
        suffix_max = [0] * (n + 1)
        # min/max has to be broken down by cage
        # n + 1 instead of n so the base case doesn't have to be treated separately
        cage_1_indexes = [n] + [i for i in range(n-1, -1, -1) if cage_index[i] == 0]
        cage_2_indexes = [n] + [i for i in range(n-1, -1, -1) if cage_index[i] == 1]
        for j, i in enumerate(cage_1_indexes[1:], start=1):
            suffix_min[i] = suffix_min[cage_1_indexes[j - 1]] + min(cells[i][0].candidates)
            suffix_max[i] = suffix_max[cage_1_indexes[j - 1]] + max(cells[i][0].candidates)
        for j, i in enumerate(cage_2_indexes[1:], start=1):
            suffix_min[i] = suffix_min[cage_2_indexes[j - 1]] + min(cells[i][0].candidates)
            suffix_max[i] = suffix_max[cage_2_indexes[j - 1]] + max(cells[i][0].candidates)


        # Bitmasks (values 1-9 -> bits 0-8)
        # Faster than Python sets for small v
        possible_masks = [0] * n
        cages_sums = (cage1.sum, cage2.sum)

        # Pruning bad sums/combos with backtrack gives ~10x performance boost
        def backtrack(idx, curr_sums, assignment):
            if idx == n:
                if curr_sums == cages_sums:
                    for i in range(n):
                        possible_masks[i] |= (1 << (assignment[i] - 1))
                return

            # O(1) remaining-sum prune
            if curr_sums[cage_index[idx]] + suffix_max[idx] < cages_sums[cage_index[idx]] or curr_sums[cage_index[idx]] + suffix_min[idx] > cages_sums[cage_index[idx]]:
                return

            for val in cells[idx][0].candidates:
                # Incremental conflict check against the previous visible cells
                if any(assignment[j] == val for j in conflicts[idx]):
                    continue
                assignment[idx] = val
                sum_to_update = cage_index[idx]
                new_sum = curr_sums[sum_to_update] + val
                new_sums = curr_sums[0:sum_to_update] + (new_sum,) + curr_sums[sum_to_update + 1:]
                backtrack(idx + 1, new_sums, assignment)

        assignment = [0] * n
        sums = (0, 0)
        backtrack(0, sums, assignment)
        eliminations = self.make_eliminations(cells, possible_masks)
        if eliminations:
            return Update(self.rule_name, self.get_explanation(cage1, cage2, eliminations), eliminations)

    def make_eliminations(self, cells, possible_masks):
        eliminations = []
        for i in range(len(cells)):
            cell = cells[i][0]
            mask = possible_masks[i]
            unused = [v for v in cell.candidates if (mask & (1 << (v - 1))) == 0]
            if unused:
                eliminations.append(Cell(cell.x, cell.y, unused))

        # Make elimination ordering more human-readable
        eliminations.sort(key=lambda x: (x.x, x.y, x.candidates[0]))
        return eliminations
   
    # Uses (cell, cage) tuple property to detect same-cage seeing 
    def cells_can_see(self, cell0, cell1):
        c0 = cell0[0]
        c1 = cell1[0]
        if c0.x == c1.x and c0.y == c1.y:
            return False  # being the same cell doesn't count
        return (cell0[1] == cell1[1] or
            c0.x == c1.x or
            c0.y == c1.y or
            (c0.x // 3 == c1.x // 3 and c0.y // 3 == c1.y // 3))

    def get_explanation(self, cage1, cage2, eliminations):
        unpacked = [Cell(c.x, c.y, [v]) for c in eliminations for v in c.candidates]
        unpacked_s = [f"{c.candidates[0]} at {str(c)}" for c in unpacked]
        value_phrase = "value is" if len(unpacked) == 1 else "values are"
        return f"When comparing {cage1} and {cage2}, the following {value_phrase} never used to form a valid arrangement of the two cages: {english_list(unpacked_s)}."