from gendiff.get_dict_diff import get_dict_diff
from tests.fixtures.dict_example import dict_1, dict_2


def test_get_dict_diff(diff_example):
    assert get_dict_diff(dict_1, dict_2) == diff_example
