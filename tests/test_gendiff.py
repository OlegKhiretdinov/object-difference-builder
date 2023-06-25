from gendiff.get_dict_diff import get_dict_diff

test_file = open('tests/fixtures/simple_obj.txt', 'r')
test_data = test_file.read()
test_file.close()

dict_1 = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": False
}

dict_2 = {
  "timeout": 20,
  "verbose": True,
  "host": "hexlet.io"
}


def test_diff_json():
    result = get_dict_diff(dict_1, dict_2)
    assert result == test_data
