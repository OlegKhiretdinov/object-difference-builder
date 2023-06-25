import json
import yaml


def get_file_content(path: str):
    file = open(path)
    file_data = None

    match path.split(".")[-1]:
        case "json":
            file_data = json.load(file)
        case "yaml" | "yml":
            file_data = yaml.load(file, Loader=yaml.CLoader)

    file.close()
    return file_data
