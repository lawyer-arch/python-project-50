import os
import textwrap

from gendiff.engine import generate_diff


def test_generate_diff_yaml():
    BASE_DIR = os.path.dirname(__file__)
    file1 = os.path.join(BASE_DIR, "fixtures", "file1.json")
    file2 = os.path.join(BASE_DIR, "fixtures", "file2.json")

    expected = textwrap.dedent("""\
    {
        common: {
          + follow: false
            setting1: Value 1
          - setting2: 200
          - setting3: true
          + setting3: null
          + setting4: blah blah
          + setting5: {
                key5: value5
            }
            setting6: {
                doge: {
                  - wow: 
                  + wow: so much
                }
                key: value
              + ops: vops
            }
        }
        group1: {
          - baz: bas
          + baz: bars
            foo: bar
          - nest: {
                key: value
            }
          + nest: str
        }
      - group2: {
            abc: 12345
            deep: {
                id: 45
            }
        }
      + group3: {
            deep: {
                id: {
                    number: 45
                }
            }
            fee: 100500
        }
    }""")

    result = generate_diff(file1, file2, format_name="stylish")
   
    print(f"Expected:\n{repr(expected)}")
    print(f"Result:\n{repr(result)}")
    assert textwrap.dedent(result).strip() == textwrap.dedent(expected).strip()