import json


def get_file_content(path_1, path_2):
    file1_data = json.load(open(path_1))
    file2_data = json.load(open(path_2))
    return file1_data, file2_data
