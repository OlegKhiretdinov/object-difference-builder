import pytest
from gendiff.diff_converter.stylish import stylish


@pytest.fixture(params=["1", "2"])
def result_string(request):
    file = open(f"tests/fixtures/stylish_result_{request.param}.txt")
    return file.read(), request.param


def test_stylish_converter(result_string, diff_example, diff_example_2):
    result, fixt_id = result_string
    if fixt_id == 1:
        assert stylish(diff_example) == result
    if fixt_id == 2:
        assert stylish(diff_example_2) == result
