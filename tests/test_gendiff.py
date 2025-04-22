import os
import textwrap
from gendiff.scripts.gendiff import generate_diff

def test_generate_diff():
    # Путь к директории, где находятся тестовые файлы
    BASE_DIR = os.path.dirname(__file__)

    # Путь к файлам с данными
    file1 = os.path.join(BASE_DIR, "fixtures", "dict1.json")
    file2 = os.path.join(BASE_DIR, "fixtures", "dict2.json")

    # Ожидаемый результат
    expected = textwrap.dedent("""\
    {
      - follow: False
      host: hexlet.io
      - proxy: 123.234.53.22
      - timeout: 50
      + timeout: 20
      + verbose: True
    }""")

    # Вызов функции generate_diff с путями к файлам
    result = generate_diff(file1, file2, format_name="stylish")

    # Сравнение результата с ожидаемым значением
    assert result.strip() == expected.strip()