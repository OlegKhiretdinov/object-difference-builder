from gendiff.get_dict_diff import get_dict_diff
from gendiff.diff_converter.stylish import stylish
from gendiff.get_file_content import get_file_content


def generate_diff(first_file, second_file, dif_format):
    file1_data = get_file_content(first_file)
    file2_data = get_file_content(second_file)
    diff = get_dict_diff(file1_data, file2_data)

    match dif_format:
        case _:
            return stylish(diff)

