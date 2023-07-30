from gendiff.get_dict_diff import get_dict_diff


def test_get_dict_diff(diff_example, dict_1, dict_2):
    assert get_dict_diff(dict_1, dict_2) == diff_example
