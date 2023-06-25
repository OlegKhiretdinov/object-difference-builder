#!/usr/bin/env python3
import json
from gendiff.cli import get_args
from gendiff.get_dict_diff import get_dict_diff


def get_file_content(path_1, path_2):
    file1_data = json.load(open(path_1))
    file2_data = json.load(open(path_2))
    return get_dict_diff(file1_data, file2_data)


def main():
    args = get_args()
    return get_file_content(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
