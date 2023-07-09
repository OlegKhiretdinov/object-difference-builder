from gendiff.get_dict_diff import get_dict_diff
from tests.fixtures.dict_example import dict_1, dict_2
from tests.fixtures.diff_eample import diff_example


def test_get_dict_diff():
    assert get_dict_diff(dict_1, dict_2) == diff_example
