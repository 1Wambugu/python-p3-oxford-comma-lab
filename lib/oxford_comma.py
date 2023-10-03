def oxford_comma(items):
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return str(items[0])
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    else:
        # Join all elements except the last one with commas
        comma_separated = ", ".join(map(str, items[:-1]))
        # Add "and" before the last element
        return f"{comma_separated}, and {items[-1]}"
