import pytest
from gendiff.diff_converter.plain import plain


@pytest.fixture
def resul_string():
    file = open("tests/fixtures/plain_result.txt")
    return file.read()


def test_converter(resul_string, diff_example):
    assert plain(diff_example) == resul_string
