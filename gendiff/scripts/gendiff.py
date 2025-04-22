import argparse
import json
import os
import yaml



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


# Функция для форматирования различий между двумя словарями
def generate_diff(dict1, dict2):
    result = []
    # Все уникальные ключи из обоих словарей
    all_keys = sorted(
        dict1.keys() | dict2.keys()
    )
    # Общие ключи у двух словарей
    shared_keys = dict1.keys() & dict2.keys()
    prefixes = {
    'unchanged': '    ',
    'removed': '  - ',
    'added': '  + ',
    }   
    for key in all_keys:
        if key in shared_keys:
            if dict1[key] == dict2[key]:
                result.append(f"{prefixes['unchanged']}{key}: {dict1[key]}")
            else:
                result.append(f"{prefixes['removed']}{key}: {dict1[key]}")
                result.append(f"{prefixes['added']}{key}: {dict2[key]}")
        elif key in dict1 and key not in dict2:
            result.append(f"{prefixes['removed']}{key}: {dict1[key]}")
        elif key in dict2 and key not in dict1:
            result.append(f"{prefixes['added']}{key}: {dict2[key]}")
    return "{\n" + "\n".join(result) + "\n}"


# Основная функция, которая принимает аргументы и сравнивает файлы
def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        '-f', '--format',
        help="set format of output",
        default="stylish"
    )
    args = parser.parse_args()

    try:
        data1 = load_file(args.first_file)
        data2 = load_file(args.second_file)
    except Exception as e:
        print(f"Ошибка: {e}")
        return

    diff = generate_diff(data1, data2)
    
    print(diff)


# Запуск программы
if __name__ == "__main__":
    main()


# from gendiff.core import run_diff
# from gendiff.loader import load_file  # сам выберет по расширению .json/.yaml
# from gendiff.diff import generate_diff
# from gendiff.formatters import format_diff

# def main():
#     run_diff(load_file, generate_diff, format_diff)