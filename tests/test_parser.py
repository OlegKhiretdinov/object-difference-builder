import pytest
from gendiff.parser import parser


@pytest.fixture(params=["json", "yml"])
def parser_params(request):
    file = open(f"tests/fixtures/file1.{request.param}")
    return file.read(), request.param


def test_parser(parser_params, dict_1):
    data, ext = parser_params
    assert parser(data, ext) == dict_1
