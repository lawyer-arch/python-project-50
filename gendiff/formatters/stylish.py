def format(diff):
    result = []
    prefixes = {
        "unchanged": "    ",
        "removed": "  - ",
        "added": "  + ",
    }

    for line in diff:
        result.append(f"{prefixes[line[0]]}{line[1]}: {line[2]}")

    return "{\n" + "\n".join(result) + "\n}"
