import os
import textwrap

from gendiff.engine import generate_diff


def test_generate_diff_plain():
    BASE_DIR = os.path.dirname(__file__)
    file1 = os.path.join(BASE_DIR, "fixtures", "file1.json")
    file2 = os.path.join(BASE_DIR, "fixtures", "file2.json")

    expected = textwrap.dedent("""
        Property 'common.follow' was added with value: false
        Property 'common.setting2' was removed
        Property 'common.setting3' was updated. From true to null
        Property 'common.setting4' was added with value: 'blah blah'
        Property 'common.setting5' was added with value: [complex value]
        Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
        Property 'common.setting6.ops' was added with value: 'vops'
        Property 'group1.baz' was updated. From 'bas' to 'bars'
        Property 'group1.nest' was updated. From [complex value] to 'str'
        Property 'group2' was removed
        Property 'group3' was added with value: [complex value]
    """)

    result = generate_diff(file1, file2, format_name="plain")
    assert result.strip() == expected.strip()