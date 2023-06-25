import json
import yaml


def get_file_handler(file_name: str):
    file_extension = file_name.split(".")[-1]
    match file_extension:
        case "json":
            return json.load
        case "yaml" | "yml":
            return lambda arg: yaml.load(arg, Loader=yaml.CLoader)


def get_file_content(path_1: str, path_2: str):
    file_1 = open(path_1)
    file_2 = open(path_2)

    file1_data = get_file_handler(path_1)(file_1)
    file2_data = get_file_handler(path_2)(file_2)
    file_1.close()
    file_2.close()

    return file1_data, file2_data
