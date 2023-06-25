#!/usr/bin/env python3
from gendiff.cli import get_args
from gendiff.get_dict_diff import get_dict_diff
from gendiff.get_file_content import get_file_content


def main():
    args = get_args()
    file1_data = get_file_content(args.first_file)
    file2_data = get_file_content(args.second_file)
    return get_dict_diff(file1_data, file2_data)


if __name__ == '__main__':
    main()
