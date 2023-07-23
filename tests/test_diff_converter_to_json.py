from json import dumps
from gendiff.diff_converter.to_json import to_json


def test_to_json(diff_example):
    assert to_json(diff_example) == dumps(diff_example)
