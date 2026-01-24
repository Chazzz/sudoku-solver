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