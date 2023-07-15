from gendiff.diff_converter.plain import plain
from tests.fixtures.diff_eample import diff_example


file = open("tests/fixtures/plain_result.txt")
plain_string = file.read()


def test_plain_converter():
    assert plain(diff_example) == plain_string
