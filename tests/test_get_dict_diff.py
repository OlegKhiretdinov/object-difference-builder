from gendiff.get_dict_diff import get_dict_diff
from tests.fixtures.dict_example import dict_1, dict_2


test_file = open('tests/fixtures/simple_obj.txt', 'r')
test_data = test_file.read()
test_file.close()


def test_diff_json():
    result = get_dict_diff(dict_1, dict_2)
    assert result == test_data
