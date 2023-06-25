from gendiff.get_file_content import get_file_content
from tests.fixtures.dict_example import dict_1


def test_get_json_file_content():
    assert get_file_content("tests/fixtures/file1.json") == dict_1


def test_get_yml_file_content():
    assert get_file_content("tests/fixtures/file1.yml") == dict_1
