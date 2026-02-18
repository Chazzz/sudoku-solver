from .innie_simple import InnieSimple
from core.coordinates import Coordinates
from core.cell import Cell
from core.cage import Cage
from core.update import Update
from core.utils import cell_combos, english_list

class CageSplittingIO(InnieSimple):
    rule_name = "Killer Cage Splitting (Innie/Outie)"
    as_score = 40
    cg_score = 75

    # If a 2+ cell innie/outie is entirely a single cage has a single,
    # split the cage into the inside cells and outside cells.
    # In future updates, cage-specific rules apply to both parts of cage.

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
        if len(straddles) != 1:
            return
        i, innie, outie = straddles[0]
        combined_cage = Cage()
        for j, cage in enumerate(row_cages):
            if i == j:
                continue
            combined_cage.coordinates += cage.coordinates
            combined_cage.sum += cage.sum
        if len(combined_cage.coordinates) + len(innie) != num_rows * 9:
            return
        others = sum([cage.sum for j, cage in enumerate(row_cages) if i != j])
        total = 45 * num_rows
        innie_value = total - others
        cage, is_inferred = self.split_cage(board, innie, outie, innie_value)
        explanation = self.get_row_explanation(
            row_start, row_end, total, others, is_inferred, innie, innie_value)
        return Update(self.rule_name, explanation, cages=[cage])

    def get_row_explanation(self, row_start, row_end, total, others, is_inferred, c, value):
        x0 = Cell.int_to_row(row_start)
        x1 = Cell.int_to_row(row_end)
        row_text = ""
        row_sum_text = ""
        cage = f"{[str(v) for v in c]}"
        if x0 == x1:
            row_text = f"Row {x0} forms a cage which adds to {total}"
            row_sum_text = f"and all cages containing the row except for {cage} sum to {others}"
        else:
            row_text = f"Rows {x0}-{x1} form a cage which adds to {total}"
            row_sum_text = f"and all cages containing the rows except for {cage} sum to {others}"
        return f"{row_text}, {row_sum_text}, making inferred cage {cage} sum to {value}."

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
        if len(straddles) != 1:
            return
        i, innie, outie = straddles[0]
        combined_cage = Cage()
        for j, cage in enumerate(col_cages):
            if i == j:
                continue
            combined_cage.coordinates += cage.coordinates
            combined_cage.sum += cage.sum
        if len(combined_cage.coordinates) + len(innie) != num_cols * 9:
            return
        others = sum([cage.sum for j, cage in enumerate(col_cages) if i != j])
        total = 45 * num_cols
        innie_value = total - others
        cage, is_inferred = self.split_cage(board, innie, outie, innie_value)
        explanation = self.get_col_explanation(
            col_start, col_end, total, others, is_inferred, innie, innie_value)
        return Update(self.rule_name, explanation, cages=[cage])

    def get_col_explanation(self, col_start, col_end, total, others, is_inferred, c, value):
        y0 = Cell.int_to_col(col_start)
        y1 = Cell.int_to_col(col_end)
        col_text = ""
        col_sum_text = ""
        cage = f"{[str(v) for v in c]}"
        if y0 == y1:
            col_text = f"Column {y0} forms a cage which adds to {total}"
            col_sum_text = f"and all cages containing the column except for {cage} sum to {others}"
        else:
            col_text = f"Columns {y0}-{y1} form a cage which adds to {total}"
            col_sum_text = f"and all cages containing the columns except for {cage} sum to {others}"
        return f"{col_text}, {col_sum_text}, making {cage} equal to {value}."

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
        if len(straddles) != 1:
            return
        i, innie, outie = straddles[0]
        combined_cage = Cage()
        for j, cage in enumerate(box_cages):
            if i == j:
                continue
            combined_cage.coordinates += cage.coordinates
            combined_cage.sum += cage.sum
        if len(combined_cage.coordinates) + len(innie) != num_boxes * 9:
            return
        others = sum([cage.sum for j, cage in enumerate(box_cages) if i != j])
        total = 45 * num_boxes
        innie_value = total - others
        cage, is_inferred = self.split_cage(board, innie, outie, innie_value)
        explanation = self.get_box_explanation(
            boxes, total, others, is_inferred, innie, innie_value)
        return Update(self.rule_name, explanation, cages=[cage])

    def get_box_explanation(self, boxes, total, others, is_inferred, c, value):
        box_sum = 45 * len(boxes)
        combined_cage_sum = box_sum - value
        box_text = ""
        box_sum_text = ""
        cage = f"{[str(v) for v in c]}"
        if len(boxes) == 1:
            box_text = f"Box {english_list(boxes)} forms a cage which adds to {total}"
            box_sum_text = f"and all cages containing the box except for {cage} sum to {others}"
        else:
            box_text = f"Boxes {english_list(boxes)} form a cage which adds to {total}"
            box_sum_text = f"and all cages containing the boxes except for {cage} sum to {others}"
        return f"{box_text}, {box_sum_text}, making {cage} equal to {value}."

    def split_cage(self, board, innie, outie, innie_value):
        for c in board.cages:
            if innie in c and outie in c:
                is_inferred = False
                scs = []
                outie_value = None
                for sc in c.subcages:
                    if innie in sc and outie in sc:
                        outie_value = sc.sum - innie_value
                        is_inferred = True
                    else:
                        scs.append(sc)
                if not outie_value:
                    outie_value = c.sum - innie_value
                scs += [Cage(innie, innie_value), Cage(outie, outie_value)]
                return Cage(c.coordinates, c.sum, scs), is_inferred