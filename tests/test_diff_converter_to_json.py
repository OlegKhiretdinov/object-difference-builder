from json import dumps
from gendiff.diff_converter.to_json import to_json
from tests.fixtures.diff_example import diff_example


file = open("tests/fixtures/stylish_result.txt")
stylish_string = file.read()


def test_to_json():
    assert to_json(diff_example) == dumps(diff_example)