from .rule import Rule
from core.coordinates import Coordinates
from core.cell import Cell
from core.update import Update
from core.utils import cell_combos, english_list

class CapturedCandidatesInvertedHard(Rule):
    rule_name = "Killer Captured Candidates 2 (Hard)"
    as_score = 20
    cg_score = 65  # 25 complexity but intense computation costs 

    # This is basically "hidden cage combinations"
    # (compare to hidden singles/doubles/triples)
    # If a row/column/box locks candidate(s) into a single cage
    # Eliminate all candidates which can't be in the cage with locked candidate(s)

    # In addition, it uses the hard algorithm properties
    # where it considers only valid permutations
    # (all candidates must be in valid coords *and*
    # locked candidates must be in the captured coords)
    def find_update(self, board):
        for check in (self.check_rows, self.check_cols, self.check_boxes):
            update = check(board)
            if update:
                return update
        return Update(self.rule_name)
    
    def check_rows(self, board):
        for i in range(9):
            unit_cells = []
            for c in board:
                if c.y == i:
                    unit_cells.append(c)
            update = self.check_unit(board, unit_cells, "row")
            if update:
                return update
    
    def check_cols(self, board):
        for i in range(9):
            unit_cells = []
            for c in board:
                if c.x == i:
                    unit_cells.append(c)
            update = self.check_unit(board, unit_cells, "column")
            if update:
                return update
    
    def check_boxes(self, board):
        for i in range(9):
            unit_cells = []
            for c in board:
                if c.x // 3 == i % 3 and c.y // 3 == i // 3:
                    unit_cells.append(c)
            update = self.check_unit(board, unit_cells, "box")
            if update:
                return update
    
    def check_unit(self, board, cells, unit_name):
        # get all cages which contain 2+ cells in unit
        # iterate values 1-9
        # if value is in only one cage and in multiple cells in cage
        # mark cage as "capturing" value
        # then for all cages with captured values
        # run hard combinations with captured constraints to find any eliminations
        cages = []
        for cage in board.cages:
            times_seen = 0
            for c in cells:
                if Coordinates(c.x, c.y) in cage.coordinates:
                    times_seen += 1
                    if times_seen == 2:
                        cages.append(cage)

        for cage in cages:
            captured = []
            captured_cells = [c for c in cells if c in cage]
            for v in range(1, 10):
                in_cage_count = 0
                out_cage_count = 0
                for c in cells:
                    if v in c.candidates:
                        if c in cage:
                            in_cage_count += 1
                        else:
                            out_cage_count += 1
                if in_cage_count > 1 and out_cage_count == 0:
                    captured.append(v)
            update = self.check_cage_optimized(board, cage, captured, captured_cells, unit_name)
            if update:
                return update
    
    def check_cage_optimized(self, board, cage, captured, captured_cells, unit_name):
        # check_cage_optimized needs some customizations so can't be inherited
        must_conditions = [(v, captured_cells) for v in captured]

        # MRV heuristic: try cells with fewest candidates first
        cells = [c for c in board if Coordinates(c.x, c.y) in cage.coordinates]
        cells.sort(key=lambda x: len(x.candidates))
        n = len(cells)

        # Precompute must conditions for low-overhead checking
        # Not clear how much improvement this is
        coord_to_idx = {(cells[i].x, cells[i].y): i for i in range(n)}
        must_reqs = []  # list of (required_val, [list_of_indices])
        for required_val, required_coords in must_conditions:
            indices = []
            for rc in required_coords:
                # Accept Coordinates object or plain (x, y) tuple
                key = (rc.x, rc.y) if hasattr(rc, 'x') else rc
                if key in coord_to_idx:
                    indices.append(coord_to_idx[key])
            if indices:
                must_reqs.append((required_val, indices))

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

        possible_masks = [0] * n

        # Fast leaf check - no dict creation, just integer access
        def satisfies_must_conditions(assignment):
            for required_val, idx_list in must_reqs:
                if not any(assignment[i] == required_val for i in idx_list):
                    return False
            return True

        def backtrack(idx, curr_sum, assignment):
            if idx == n:
                if curr_sum == cage.sum and satisfies_must_conditions(assignment):
                    for i in range(n):
                        possible_masks[i] |= (1 << (assignment[i] - 1))
                return

            # O(1) remaining-sum prune
            if curr_sum + suffix_max[idx] < cage.sum or curr_sum + suffix_min[idx] > cage.sum:
                return

            for val in cells[idx].candidates:
                if any(assignment[j] == val for j in conflicts[idx]):
                    continue
                assignment[idx] = val
                backtrack(idx + 1, curr_sum + val, assignment)

        assignment = [0] * n
        backtrack(0, 0, assignment)

        eliminations = self.make_eliminations(cells, possible_masks)
        if eliminations:
            return Update(self.rule_name, self.get_explanation(captured, captured_cells, unit_name, cage, eliminations), eliminations)

    def check_cage_optimized_old(self, board, cage, captured, captured_cells, unit_name):
        # check_cage_optimized needs some customizations so can't be inherited

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

        must_conditions = [(v, captured_cells) for v in captured]
        def satisfies_must_conditions(assignment):
            # Build a map: coordinate -> value in this assignment
            coord_to_val = {(cells[i].x, cells[i].y): assignment[i]
                            for i in range(n)}
            for required_val, required_coords in must_conditions:
                found = False
                for rc in required_coords:
                    key = (rc.x, rc.y)
                    if coord_to_val.get(key) == required_val:
                        found = True
                        break
                if not found:
                    return False
            return True

        # Pruning bad sums/combos with backtrack gives ~10x performance boost
        def backtrack(idx, curr_sum, assignment):
            if idx == n:
                if curr_sum == cage.sum and satisfies_must_conditions(assignment):
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
            return Update(self.rule_name, self.get_explanation(captured, captured_cells, unit_name, cage, eliminations), eliminations)


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

    def get_explanation(self, captured, captured_cells, unit_name, cage, eliminations):
        is_are = "is" if len(captured) == 1 else "are" 
        s1 = f"Given {english_list(captured)} {is_are} only possible in {english_list(captured_cells)} for all cells in that {unit_name}, {english_list(captured)} must be in cage {cage}."

        unpacked = [Cell(c.x, c.y, [v]) for c in eliminations for v in c.candidates]
        unpacked_s = [f"{c.candidates[0]} at {str(c)}" for c in unpacked]
        value_word = "Value" if len(unpacked) == 1 else "Values"
        return f"{s1} With that requirement, the following values are never used to form a valid sum in cage {cage}: {english_list(unpacked_s)}."

        
