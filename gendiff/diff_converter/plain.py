from string import Template
from gendiff.consts import PROPERTY_STATUS


ADDED_TMPL = Template("Property '$name' was added with value: $value")
DELETED_TMPL = Template("Property '$name' was removed")
CHANGED_TMPL = Template("Property '$name' was updated. From $init_value to "
                        "$current_value")


def get_string_value(values, name):
    if isinstance(values, list):
        return "[complex value]"
    elif isinstance(values[name], list):
        return "[complex value]"
    elif isinstance(values[name], str):
        return f"'{values[name]}'"
    else:
        return values[name]


def plain(diff, parent_name=""):
    result = []
    for prop in diff:
        status = prop["status"]
        name = f'{parent_name}{"." if parent_name else ""}{prop["name"]}'
        values = prop["values"]

        match status:
            case PROPERTY_STATUS.DELETED:
                result.append(DELETED_TMPL.substitute(name=name))
            case PROPERTY_STATUS.ADDED:
                result.append(
                    ADDED_TMPL.substitute(
                        name=name,
                        value=get_string_value(values, "current")
                    )
                )
            case PROPERTY_STATUS.CHANGED:
                if isinstance(values, list):
                    result.append(plain(prop["values"], parent_name=name))
                else:
                    result.append(
                        CHANGED_TMPL.substitute(
                            name=name,
                            init_value=get_string_value(values, "initial"),
                            current_value=get_string_value(values, "current")
                        )
                    )
            case _:
                pass

    return '\n'.join(result)\
        .replace(" False", " false")\
        .replace(" True", " true")\
        .replace(" None", " null")
