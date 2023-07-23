import pytest
from gendiff.diff_converter.stylish import stylish


@pytest.fixture
def result_string():
    file = open("tests/fixtures/stylish_result.txt")
    return file.read()


def test_stylish_converter(result_string, diff_example):
    assert stylish(diff_example) == result_string
