import json

def format_json(diff_tree):
    return json.dumps(diff_tree, indent=2)