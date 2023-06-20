#!/usr/bin/env python3
from gendiff.cli import get_args
import json


def get_file_content(path_1, path_2):
    file1_data = json.load(open(path_1))
    file2_data = json.load(open(path_2))
    result = "{\n"
    keys1 = list(file1_data)
    keys2 = list(file2_data)
    keys1.sort()
    keys2.sort()

    for i in keys1:
        if i not in keys2:
            result += f'  - {i}: {file1_data[i]}\n'
        elif file1_data[i] == file2_data[i]:
            result += f'    {i}: {file1_data[i]}\n'
        else:
            result += f'  - {i}: {file1_data[i]}\n'
            result += f'  + {i}: {file2_data[i]}\n'

    for i in keys2:
        if i not in keys1:
            result += f'  + {i}: {file2_data[i]}\n'

    result += "}"

    return result


def main():
    args = get_args()
    return get_file_content(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
