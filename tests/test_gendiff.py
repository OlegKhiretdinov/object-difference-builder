from gendiff.gendiff import get_file_content


def test_get_file_content():
    test_file = open('tests/fixtures/simple_obj.txt', 'r')
    test_data = test_file.read()
    test_file.close()
    result = get_file_content("tests/fixtures/file1.json", "tests/fixtures/file2.json")
    print(test_data)
    print(result)
    assert result == test_data
