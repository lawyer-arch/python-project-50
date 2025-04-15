import argparse
import json
import os

# Функция для загрузки данных из JSON файла
def load_json(filepath):
    with open(os.path.expanduser(filepath), 'r') as f:
        return json.load(f)

# Функция для форматирования различий между двумя словарями
def format_diff(dict1, dict2):
    result = []
    all_keys = sorted(dict1.keys() | dict2.keys())  # Все уникальные ключи из обоих словарей
    shared_key = dict1.keys() & dict2.keys()  # Общие ключи у двух словарей

    for key in all_keys:
        if key in shared_key:
            if dict1[key] == dict2[key]:
                result.append(f"  {key}: {dict1[key]}")
            else:
                result.append(f"  - {key}: {dict1[key]}")
                result.append(f"  + {key}: {dict2[key]}")
        elif key in dict1:
            result.append(f"  - {key}: {dict1[key]}")
        elif key in dict2:
            result.append(f"  + {key}: {dict2[key]}")
    return "{\n" + "\n".join(result) + "\n}"

# Основная функция, которая принимает аргументы и сравнивает файлы
def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")  # Путь к первому файлу
    parser.add_argument("second_file")  # Путь ко второму файлу
    parser.add_argument('-f', '--format', help="set format of output")  # Формат вывода
    args = parser.parse_args()

    # Загружаем данные из файлов
    data1 = load_json(args.first_file)
    data2 = load_json(args.second_file)

    # Выводим различия между файлами
    print(format_diff(data1, data2))

# Запуск программы
if __name__ == "__main__":
    main()