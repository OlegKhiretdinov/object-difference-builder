from gendiff.diff_converter.stylish import stylish
from tests.fixtures.diff_example import diff_example


file = open("tests/fixtures/stylish_result.txt")
stylish_string = file.read()


def test_stylish_converter():
    assert stylish(diff_example) == stylish_string
