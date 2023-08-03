import pytest
from gendiff.diff_converter.plain import plain


@pytest.fixture(params=["1", "2"])
def result_string(request):
    file = open(f"tests/fixtures/plain_result_{request.param}.txt")
    return file.read(), request.param


def test_plain_converter(result_string, diff_example, diff_example_2):
    result, fixt_id = result_string
    if fixt_id == 1:
        assert plain(diff_example) == result
    if fixt_id == 2:
        assert plain(diff_example_2) == result
