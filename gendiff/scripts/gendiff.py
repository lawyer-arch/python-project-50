import argparse
import json
import os


# Функция для загрузки данных из JSON файла
def load_json(filepath):
    with open(os.path.expanduser(filepath), 'r') as f:
        return json.load(f)


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
    parser.add_argument("first_file")  # Путь к первому файлу
    parser.add_argument("second_file")  # Путь ко второму файлу
    # Формат вывода
    parser.add_argument(
        '-f', '--format', 
        help="set format of output"
    )
    args = parser.parse_args()

    # Загружаем данные из файлов
    data1 = load_json(args.first_file)
    data2 = load_json(args.second_file)

    # Выводим различия между файлами
    print(generate_diff(data1, data2))


# Запуск программы
if __name__ == "__main__":
    main()