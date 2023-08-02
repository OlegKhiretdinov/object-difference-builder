import pytest
from gendiff.diff_converter.plain import plain


@pytest.fixture(params=["1"])
def resul_string(request):
    file = open(f"tests/fixtures/plain_result_{request.param}.txt")
    return file.read(), request.param


def test_converter(resul_string, diff_example):
    result, fixt_ = resul_string
    assert plain(diff_example) == result
