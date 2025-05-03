import json
import os

from gendiff.engine import generate_diff


def test_generate_diff_plain():
    BASE_DIR = os.path.dirname(__file__)
    file1 = os.path.join(BASE_DIR, "fixtures", "file1.json")
    file2 = os.path.join(BASE_DIR, "fixtures", "file2.json")

    expected_data = ("""[
    {
      "key": "common",
      "type": "nested",
      "children": [
        {
          "key": "follow",
          "type": "added",
          "value": false
        },
        {
          "key": "setting1",
          "type": "unchanged",
          "value": "Value 1"
        },
        {
          "key": "setting2",
          "type": "removed",
          "value": 200
        },
        {
          "key": "setting3",
          "type": "changed",
          "old_value": true,
          "new_value": null
        },
        {
          "key": "setting4",
          "type": "added",
          "value": "blah blah"
        },
        {
          "key": "setting5",
          "type": "added",
          "value": {
            "key5": "value5"
          }
        },
        {
          "key": "setting6",
          "type": "nested",
          "children": [
            {
              "key": "doge",
              "type": "nested",
              "children": [
                {
                  "key": "wow",
                  "type": "changed",
                  "old_value": "",
                  "new_value": "so much"
                }
              ]
            },
            {
              "key": "key",
              "type": "unchanged",
              "value": "value"
            },
            {
              "key": "ops",
              "type": "added",
              "value": "vops"
            }
          ]
        }
      ]
    },
    {
      "key": "group1",
      "type": "nested",
      "children": [
        {
          "key": "baz",
          "type": "changed",
          "old_value": "bas",
          "new_value": "bars"
        },
        {
          "key": "foo",
          "type": "unchanged",
          "value": "bar"
        },
        {
          "key": "nest",
          "type": "changed",
          "old_value": {
            "key": "value"
          },
          "new_value": "str"
        }
      ]
    },
    {
      "key": "group2",
      "type": "removed",
      "value": {
        "abc": 12345,
        "deep": {
          "id": 45
        }
      }
    },
    {
      "key": "group3",
      "type": "added",
      "value": {
        "deep": {
          "id": {
            "number": 45
          }
        },
        "fee": 100500
      }
    }
    ]""")

    expected = json.dumps(expected_data, indent=2)
    result = generate_diff(file1, file2, format_name="json")
    assert result == expected