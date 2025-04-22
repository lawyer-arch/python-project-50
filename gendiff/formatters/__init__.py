from .stylish import format as format_stylish


def get_formatter(name):
    if name == "stylish":
        return format_stylish
    raise ValueError(f"Неизвестный формат: {name}")
