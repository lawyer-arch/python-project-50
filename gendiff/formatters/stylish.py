def format_stylish(diff):
    result = []
    prefixes = {
        "unchanged": "  ",
        "removed": "  - ",
        "added": "  + ",
    }

    # ✅ Сортируем diff по ключу (line[1])
    diff = sorted(diff, key=lambda x: x[1])

    for line in diff:
        result.append(f"{prefixes[line[0]]}{line[1]}: {line[2]}")

    return "{\n" + "\n".join(result) + "\n}"
