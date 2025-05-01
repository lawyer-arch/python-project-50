def stringify_plain(value):
    if isinstance(value, (dict, list, set, tuple)):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, str):
        return f"'{value}'"
    

def format_plain(diff, path=""):
    lines = []
    for node in diff:
        node_type = node["type"]
        key = node["key"]
        new_path = f"{path}.{key}" if path else key
        
        if node_type == "nested":
            if "children" in node:
                lines.extend(format_plain(node["children"], new_path))
        elif node_type == "removed":
            lines.append(f"Property '{new_path}' was removed")
        elif node_type == "added":
            lines.append(
                f"Property '{new_path}' was added "
                f"with value: {stringify_plain(node.get('value'))}"
            )
        elif node_type == "changed":
            old_value = node.get("old_value")
            new_value = node.get("new_value")
            lines.append(
                f"Property '{new_path}' was updated. "
                f"From {stringify_plain(old_value)} "
                f"to {stringify_plain(new_value)}"
            )
        else:
            pass
    return lines


def to_plain_string(diff):
    lines = format_plain(diff)
    return '\n'.join(lines) + '\n' if lines else ''