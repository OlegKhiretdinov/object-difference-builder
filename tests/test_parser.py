from gendiff.parser import parser
from tests.fixtures.dict_example import dict_1


def test_get_json_file_content():
    assert parser("tests/fixtures/file1.json", ) == dict_1


def test_get_yml_file_content():
    assert parser("tests/fixtures/file1.yml", ) == dict_1
