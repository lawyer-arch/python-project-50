import json


def formater_json(diff_tree):
    return json.dumps(diff_tree, indent=2)