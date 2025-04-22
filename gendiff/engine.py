from .formatters import get_formatter

from .loader import load_file


def generate_diff(path1, path2, format_name='stylish'):
    dict1 = load_file(path1)
    dict2 = load_file(path2)
    
    diff = []
    all_keys = sorted(dict1.keys() | dict2.keys())
    shared_keys = dict1.keys() & dict2.keys()
    
    for key in all_keys:
        if key in shared_keys:
            if dict1[key] == dict2[key]:
                diff.append(('unchanged', key, dict1[key]))
            else:
                diff.append(('removed', key, dict1[key]))
                diff.append(('added', key, dict2[key]))
        elif key in dict1:
            diff.append(('removed', key, dict1[key]))
        else:
            diff.append(('added', key, dict2[key]))

    formatter = get_formatter(format_name)
    return formatter(diff)

