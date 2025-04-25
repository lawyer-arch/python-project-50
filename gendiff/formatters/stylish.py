def get_indent(depth):
    return " " * (depth * 4)


def stringify(value, depth):
    if isinstance(value, dict):
        lines = [
            f"{get_indent(depth + 1)}  {k}: {stringify(v, depth + 1)}"
            for k, v in value.items()
        ]
        return "\n" + "\n".join(lines) + f"\n{get_indent(depth)}"
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def format_stylish(diff, depth=0):
    
    def format_line(key, value, depth, prefix=' '):
        indent = get_indent(depth)
        if isinstance(value, dict):
            lines = [f"{indent}  {prefix} {key}: {{"]
            for k, v in value.items():
                lines.append(format_line(k, v, depth + 1))
            lines.append(f"{get_indent(depth + 1)}}}")
            return "\n".join(lines)
        else:
            return f"{indent}  {prefix} {key}: {stringify(value, depth)}"
        
    lines = []

    for node in diff:
        key = node["key"]
        node_type = node["type"]

        if node_type == "nested":
            children = format_stylish(node["children"], depth + 1)
            lines.append(f"{get_indent(depth)}    {key}: {children}")
        elif node_type == "unchanged":
            lines.append(format_line(key, node["value"], depth, ' '))
        elif node_type == "removed":
            lines.append(format_line(key, node["value"], depth, '-'))
        elif node_type == "added":
            lines.append(format_line(key, node["value"], depth, '+'))
        elif node_type == "changed":
            lines.append(format_line(key, node["old_value"], depth, '-'))
            lines.append(format_line(key, node["new_value"], depth, '+'))

    return f"{{\n{'\n'.join(lines)}\n{get_indent(depth)}}}"