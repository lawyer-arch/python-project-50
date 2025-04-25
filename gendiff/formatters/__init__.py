from .stylish import format_stylish
# from .plain import format_plain
# from .json import format_json

def get_formatter(format_name):
    if format_name == 'stylish':
        return format_stylish
    # elif format_name == 'plain':
    #     return format_plain
    # elif format_name == 'json':
    #     return format_json
    raise ValueError(f"Unsupported format: {format_name}")
