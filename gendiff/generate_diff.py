from gendiff.get_dict_diff import get_dict_diff
from gendiff.parser import parse
from gendiff.diff_converter.stylish import stylish
from gendiff.diff_converter.plain import plain
from gendiff.diff_converter.to_json import to_json


def get_file_content(path):
    with open(path) as f:
        parsed_data = parse(f.read(), path.split(".")[-1])
    return parsed_data


def generate_diff(first_file, second_file, output_format="stylish"):
    first_parsed_data = get_file_content(first_file)
    second_parsed_data = get_file_content(second_file)
    diff = get_dict_diff(first_parsed_data, second_parsed_data)

    match output_format:
        case "plain":
            return plain(diff)
        case "json":
            return to_json(diff)
        case "stylish":
            return stylish(diff)
        case _:
            return None
