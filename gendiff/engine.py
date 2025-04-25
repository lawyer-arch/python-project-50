from .loader import load_file
from .formatters import get_formatter
from .diff_builder import build_diff


def generate_diff(path1, path2, format_name="stylish"):
    dict1 = load_file(path1) if not isinstance(path1, dict) else path1
    dict2 = load_file(path2) if not isinstance(path2, dict) else path2

    diff = build_diff(dict1, dict2)

    formatter = get_formatter(format_name)
    print(f"Result:\n{repr(formatter(diff))}")
    return formatter(diff)
