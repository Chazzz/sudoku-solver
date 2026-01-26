from functools import cache

def english_list(values):
    if not values:
        return ""
    elif len(values) == 1:
        return str(values[0])
    elif len(values) == 2:
        return f"{values[0]} and {values[1]}"
    else:
        # Join all but last with comma, then "and last"
        return f"{', '.join(str(x) for x in values[:-1])}, and {values[-1]}"

def make_cell_combos():
    # {(size, sum): [combos]}
    cell_combos = {}
    for i in range(1, 2 ** 9):
        combo = []
        for j in range(9):
            if i // (2 ** j) % 2 == 1:
                combo.append(j + 1)
        key = (len(combo), sum(combo))
        if key in cell_combos:
            cell_combos[key].append(combo)
        else:
            cell_combos[key] = [combo]
    return cell_combos

cell_combos = make_cell_combos()