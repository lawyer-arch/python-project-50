import os
import textwrap

from gendiff.engine import generate_diff


def test_generate_diff_yaml():
    BASE_DIR = os.path.dirname(__file__)
    file1 = os.path.join(BASE_DIR, "fixtures", "json_to_yaml1.yaml")
    file2 = os.path.join(BASE_DIR, "fixtures", "json_to_yaml2.yaml")

    expected = textwrap.dedent("""\
    {
      - follow: false
        host: hexlet.io
      - proxy: 123.234.53.22
      - timeout: 50
      + timeout: 20
      + verbose: true
    }""")

    result = generate_diff(file1, file2, format_name="stylish")
    print(repr(result))
    assert textwrap.dedent(result).strip() == textwrap.dedent(expected).strip()
