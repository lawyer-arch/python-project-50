import json
import yaml
import os

############ Формируем словарь для обработки #############

def load_file(file_path):
    _, ext = os.path.splitext(file_path)

    with open(file_path, 'r') as f:
        if ext in ['.yaml', '.yml']:
            data = yaml.safe_load(f)
        elif ext == '.json':
            data = json.load(f)
        else:
            raise ValueError(f"Неподдерживаемый формат файла: {ext}")

    if not isinstance(data, dict):
        raise ValueError(f"Ожидался словарь, но получен {type(data).__name__} в файле {file_path}")
    return data

# print(load_file()) для проверки