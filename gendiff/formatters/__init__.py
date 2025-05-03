from .plain import to_plain_string
from .stylish import format_stylish
from .json import format_json


def get_formatter(format_name):
    if format_name == 'stylish':
        return format_stylish
    elif format_name == 'plain':
        return to_plain_string
    elif format_name == 'json':
        return format_json
    raise ValueError(f"Unsupported format: {format_name}")
