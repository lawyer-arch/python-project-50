def build_diff(dict1, dict2):
    diff = []
    keys = sorted(dict1.keys() | dict2.keys())

    for key in keys:
        if key in dict1 and key in dict2:
            val1, val2 = dict1[key], dict2[key]

            if isinstance(val1, dict) and isinstance(val2, dict):
                diff.append({
                    "key": key,
                    "type": "nested",
                    "children": build_diff(val1, val2)
                })
            elif val1 == val2:
                diff.append({
                    "key": key,
                    "type": "unchanged",
                    "value": val1
                })
            else:
                diff.append({
                    "key": key,
                    "type": "changed",
                    "old_value": val1,
                    "new_value": val2
                })

        elif key in dict1:
            diff.append({
                "key": key,
                "type": "removed",
                "value": dict1[key]
            })
        else:
            diff.append({
                "key": key,
                "type": "added",
                "value": dict2[key]
            })

    return diff
