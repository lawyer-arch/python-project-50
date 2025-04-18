import re
from gendiff.scripts.gendiff import generate_diff

def test_generate_diff():
    dict1 = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }
    dict2 = {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    }

    expected = '''{
      - follow: False
      host: hexlet.io
      - proxy: 123.234.53.22
      - timeout: 50
      + timeout: 20
      + verbose: True
    }'''

    def normalize_string(s):
        # Убираем лишние пробелы в начале и в конце строк и нормализуем пробелы
        return re.sub(r'\s+', ' ', s.strip())

    assert normalize_string(generate_diff(dict1, dict2)) == \
           normalize_string(expected)