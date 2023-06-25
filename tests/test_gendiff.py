from gendiff.gen_diff import get_file_content

test_file = open('tests/fixtures/simple_obj.txt', 'r')
test_data = test_file.read()
test_file.close()


def test_diff_json():
    result = get_file_content("tests/fixtures/file1.json", "tests/fixtures/file2.json")
    assert result == test_data
