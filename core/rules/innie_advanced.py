from .rule import Rule
from core.update import Update
from core.cell import Cell
from core.cage import Cage
from core.coordinates import Coordinates
from core.utils import english_list
from functools import cache

class InnieAdvancedTemplate(Rule):
    rule_name = "Killer Innie (2+ cells)"
    as_score = 30
    cg_score = 1000 # was 55, do not run
    min_innie = None
    max_innie = None

    # for each row, column and box
    # get all cages in that 9-group
    # Then look at all (n-1) subgroups
    # For each group, innies are the cells
    # inside the group in cages straddling the group
    # Calculates the hard combinations for that innie
    def find_update(self, board):
        for check in (self.check_rows, self.check_cols, self.check_boxes):
            update = check(board)
            if update:
                return update
        return Update(self.rule_name)
    
    def check_rows(self, board):
        for row_start in range(9):
            for row_end in range(row_start, 9):
                update = self.check_row_range(board, row_start, row_end)
                if update:
                    return update
        return None

    def check_row_range(self, board, row_start, row_end):
        row_cages = []
        for cage in board.cages:
            if cage.subcages:
                for sc in cage.subcages:
                    if any(row_start <= c.y <= row_end for c in sc.coordinates):
                        row_cages.append(sc)
            else:
                if any(row_start <= c.y <= row_end for c in cage.coordinates):
                    row_cages.append(cage)
        return self.check_row_cages(board, row_start, row_end, row_cages)

    def check_row_cages(self, board, row_start, row_end, row_cages):
        num_rows = 1 + row_end - row_start
        straddles = []
        for i, v in enumerate(row_cages):
            innie = [c for c in v.coordinates if (row_start <= c.y <= row_end)]
            outie = [c for c in v.coordinates if not (row_start <= c.y <= row_end)]
            if innie and outie:
                straddles.append((i, innie, outie))
        indexes = [s[0] for s in straddles]
        innies = [c for s in straddles for c in s[1]]
        outies = [c for s in straddles for c in s[2]]
        combined_cage = Cage()
        for j, cage in enumerate(row_cages):
            if j not in indexes:
                combined_cage.coordinates += cage.coordinates
                combined_cage.sum += cage.sum
        if len(combined_cage.coordinates) + len(innies) != num_rows * 9:
            return
        others = combined_cage.sum
        total = 45 * num_rows
        innie_value = total - others
        eliminations = self.check_cells_optimized(innies, board, innie_value)
        if eliminations:
            explanation = self.get_row_explanation(
                row_start, row_end, total, others, innies, innie_value, eliminations)
            return Update(self.rule_name, explanation, eliminations)
        
    def get_row_explanation(self, row_start, row_end, total, others, c, value, eliminations):
        x0 = Cell.int_to_row(row_start)
        x1 = Cell.int_to_row(row_end)
        row_text = ""
        row_sum_text = ""
        cells = f"{[str(v) for v in c]}"
        if x0 == x1:
            row_text = f"Row {x0} forms a cage which adds to {total}"
            row_sum_text = f"and all cages containing the row except for {cells} sum to {others}"
        else:
            row_text = f"Rows {x0}-{x1} form a cage which adds to {total}"
            row_sum_text = f"and all cages containing the rows except for {cells} sum to {others}"
        unpacked = [Cell(c.x, c.y, [v]) for c in eliminations for v in c.candidates]
        unpacked_s = [f"{c.candidates[0]} at {str(c)}" for c in unpacked]
        value_text = f"The following values are never used to form a valid sum in cells {cells}: {english_list(unpacked_s)}."
        return f"{row_text}, {row_sum_text}, making cells {cells} sum to {value}. {value_text}"

    def check_cols(self, board):
        for col_start in range(9):
            for col_end in range(col_start, 9):
                update = self.check_col_range(board, col_start, col_end)
                if update:
                    return update
        return None

    def check_col_range(self, board, col_start, col_end):
        col_cages = []
        for cage in board.cages:
            if cage.subcages:
                for sc in cage.subcages:
                    if any(col_start <= c.x <= col_end for c in sc.coordinates):
                     col_cages.append(sc)
            else:
                if any(col_start <= c.x <= col_end for c in cage.coordinates):
                    col_cages.append(cage)
        return self.check_col_cages(board, col_start, col_end, col_cages)

    def check_col_cages(self, board, col_start, col_end, col_cages):
        num_cols = 1 + col_end - col_start
        straddles = []
        for i, v in enumerate(col_cages):
            innie = [c for c in v.coordinates if (col_start <= c.x <= col_end)]
            outie = [c for c in v.coordinates if not (col_start <= c.x <= col_end)]
            if innie and outie:
                straddles.append((i, innie, outie))
        indexes = [s[0] for s in straddles]
        innies = [c for s in straddles for c in s[1]]
        outies = [c for s in straddles for c in s[2]]
        if len(innies) > 9:
            return
        combined_cage = Cage()
        for j, cage in enumerate(col_cages):
            if j not in indexes:
                combined_cage.coordinates += cage.coordinates
                combined_cage.sum += cage.sum
        if len(combined_cage.coordinates) + len(innies) != num_cols * 9:
            return
        others = combined_cage.sum
        total = 45 * num_cols
        innie_value = total - others
        eliminations = self.check_cells_optimized(innies, board, innie_value)
        if eliminations:
            explanation = self.get_col_explanation(
                col_start, col_end, total, others, innies, innie_value, eliminations)
            return Update(self.rule_name, explanation, eliminations)
         
    def get_col_explanation(self, col_start, col_end, total, others, c, value, eliminations):
        y0 = Cell.int_to_col(col_start)
        y1 = Cell.int_to_col(col_end)
        col_text = ""
        col_sum_text = ""
        cells = f"{[str(v) for v in c]}"
        if y0 == y1:
            col_text = f"Column {y0} forms a cage which adds to {total}"
            col_sum_text = f"and all cages containing the column except for {cells} sum to {others}"
        else:
            col_text = f"Columns {y0}-{y1} form a cage which adds to {total}"
            col_sum_text = f"and all cages containing the columns except for {cells} sum to {others}"
        unpacked = [Cell(c.x, c.y, [v]) for c in eliminations for v in c.candidates]
        unpacked_s = [f"{c.candidates[0]} at {str(c)}" for c in unpacked]
        value_text = f"The following values are never used to form a valid sum in cells {cells}: {english_list(unpacked_s)}."
        return f"{col_text}, {col_sum_text}, making cells {cells} sum to {value}. {value_text}"

    def check_boxes(self, board):
        for i in range(1, 2 ** 9):
            boxes = []
            for j in range(9):
                if i // (2 ** j) % 2 == 1:
                    box_tuple = (j % 3, j // 3)
                    boxes.append(box_tuple)
            if self.is_contiguous_boxes(boxes):
                update = self.check_box_combination(board, boxes)
                if update:
                    return update
        return None

    @property
    @cache
    def box_neighbors(self):
        box_neighbors = {}
        for x in range(3):
            for y in range(3):
                neighbors = []
                if x + 1 < 3:
                    neighbors.append((x + 1, y))
                if x - 1 >= 0:
                    neighbors.append((x - 1, y))
                if y + 1 < 3:
                    neighbors.append((x, y + 1))
                if y - 1 >= 0:
                    neighbors.append((x, y - 1))
                box_neighbors[(x, y)] = neighbors
        return box_neighbors
        
    def is_contiguous_boxes(self, boxes):
        if len(boxes) == 1:
            return True
        for box in boxes:
            has_neighbor = any(b in self.box_neighbors[box] for b in boxes)
            if not has_neighbor:
                return False
        return True

    def in_boxes(self, c, boxes):
        return any(c.x // 3 == b[0] and c.y // 3 == b[1] for b in boxes)
    
    def check_box_combination(self, board, boxes):
        box_cages = []
        for cage in board.cages:
            if cage.subcages:
                for sc in cage.subcages:
                    if any(self.in_boxes(c, boxes) for c in sc.coordinates):
                        box_cages.append(sc)
            else:
                if any(self.in_boxes(c, boxes) for c in cage.coordinates):
                    box_cages.append(cage)
        return self.check_box_cages(board, boxes, box_cages)

    def check_box_cages(self, board, boxes, box_cages):
        num_boxes = len(boxes)
        straddles = []
        for i, v in enumerate(box_cages):
            innie = [c for c in v.coordinates if self.in_boxes(c, boxes)]
            outie = [c for c in v.coordinates if not self.in_boxes(c, boxes)]
            if innie and outie:
                straddles.append((i, innie, outie))
        indexes = [s[0] for s in straddles]
        innies = [c for s in straddles for c in s[1]]
        outies = [c for s in straddles for c in s[2]]
        combined_cage = Cage()
        for j, cage in enumerate(box_cages):
            if j not in indexes:
                combined_cage.coordinates += cage.coordinates
                combined_cage.sum += cage.sum
        if len(combined_cage.coordinates) + len(innies) != num_boxes * 9:
            return
        others = combined_cage.sum
        total = 45 * num_boxes
        innie_value = total - others
        eliminations = self.check_cells_optimized(innies, board, innie_value)
        if eliminations:
            explanation = self.get_box_explanation(
                boxes, total, others, innies, innie_value, eliminations)
            return Update(self.rule_name, explanation, eliminations)

    def get_box_explanation(self, boxes, total, others, c, value, eliminations):
        box_text = ""
        box_sum_text = ""
        cells = f"{[str(v) for v in c]}"
        if len(boxes) == 1:
            box_text = f"Box {english_list(boxes)} forms a cage which adds to {total}"
            box_sum_text = f"and all cages containing the box except for {cells} sum to {others}"
        else:
            box_text = f"Boxes {english_list(boxes)} form a cage which adds to {total}"
            box_sum_text = f"and all cages containing the boxes except for {cells} sum to {others}"
        unpacked = [Cell(c.x, c.y, [v]) for c in eliminations for v in c.candidates]
        unpacked_s = [f"{c.candidates[0]} at {str(c)}" for c in unpacked]
        value_text = f"The following values are never used to form a valid sum in cells {cells}: {english_list(unpacked_s)}."
        return f"{box_text}, {box_sum_text}, making cells {cells} sum to {value}. {value_text}"

    def check_cells_optimized(self, coords, board, cell_sum):
        n = len(coords)  # Precompute list length
        if not self.min_innie or not self.max_innie:
            return []  # Skip eval in template class
        if n < self.min_innie or n > self.max_innie:
            return []  # Skip eval for wrong sized innie

        # MRV heuristic: try cells with fewest candidates first
        # This prunes the search tree faster on real Killer Sudoku boards
        cells = [c for c in board if Coordinates(c.x, c.y) in coords]
        cells.sort(key=lambda x: len(x.candidates))

        # Precompute conflicts which trigger prune
        conflicts = [[] for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if self.cells_can_see(cells[i], cells[j]):
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
                if curr_sum == cell_sum:
                    for i in range(n):
                        possible_masks[i] |= (1 << (assignment[i] - 1))
                return

            # O(1) remaining-sum prune
            if curr_sum + suffix_max[idx] < cell_sum or curr_sum + suffix_min[idx] > cell_sum:
                return

            for val in cells[idx].candidates:
                # Incremental conflict check against the previous visible cells
                if any(assignment[j] == val for j in conflicts[idx]):
                    continue
                assignment[idx] = val
                backtrack(idx + 1, curr_sum + val, assignment)

        assignment = [0] * n
        backtrack(0, 0, assignment)
        return self.make_eliminations(cells, possible_masks)

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

class InnieAdvanced2(InnieAdvancedTemplate):
    cg_score = 55
    min_innie = 2
    max_innie = 2

class InnieAdvanced3(InnieAdvancedTemplate):
    cg_score = 60
    min_innie = 3
    max_innie = 3

class InnieAdvanced4(InnieAdvancedTemplate):
    cg_score = 65
    min_innie = 4
    max_innie = 4

class InnieAdvanced5(InnieAdvancedTemplate):
    cg_score = 70
    min_innie = 5
    max_innie = 5

class InnieAdvanced6(InnieAdvancedTemplate):
    cg_score = 75
    min_innie = 6
    max_innie = 6

class InnieAdvanced7(InnieAdvancedTemplate):
    cg_score = 80
    min_innie = 7
    max_innie = 7

class InnieAdvanced8(InnieAdvancedTemplate):
    cg_score = 85
    min_innie = 8
    max_innie = 8

class InnieAdvanced9(InnieAdvancedTemplate):
    cg_score = 90
    min_innie = 9
    max_innie = 9

class InnieAdvanced10(InnieAdvancedTemplate):
    cg_score = 100
    min_innie = 10
    max_innie = 100

    def find_update(self, board):
        print("Warning: InnieAdvanced10 may take a long time to compute")
        return super().find_update(board)