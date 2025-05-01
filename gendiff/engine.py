from .diff_builder import build_diff
from .formatters import get_formatter
from .loader import load_file


def normalize_data(source):
    if isinstance(source, dict):
        return source
    return load_file(source)


def generate_diff(path1, path2, format_name="stylish"):
    data1 = normalize_data(path1)
    data2 = normalize_data(path2)
    return generate_diff_from_data(data1, data2, format_name)


def generate_diff_from_data(data1, data2, format_name="stylish"):
    diff = build_diff(data1, data2)
    formatter = get_formatter(format_name)
    return formatter(diff)