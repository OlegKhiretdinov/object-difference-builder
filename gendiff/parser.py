import json
import yaml


def parser(data, parser_format):
    file_data = None

    match parser_format:
        case "json":
            file_data = json.loads(data)
        case "yaml" | "yml":
            file_data = yaml.load(data, Loader=yaml.CLoader)

    return file_data
