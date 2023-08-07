from gendiff.get_dict_diff import ADDED, DELETED, CHANGED, PRISTINE


STATUS_VALUES_RELATION = {
    ADDED: "current",
    DELETED: "initial",
    PRISTINE: "initial",
}

JSON_PREFIX = {
    ADDED: "+ ",
    DELETED: "- ",
    PRISTINE: "  ",
}

INDENT = "  "


def handle_none_pristine(name, status, value, children):
    name_str = f'{JSON_PREFIX[status]}{name}:'
    prop_str = f' {children or value[STATUS_VALUES_RELATION[status]]}'
    return f'{name_str}{prop_str}'


def stylish(diff, level=1):
    result = "{\n"

    for prop in diff:
        values = prop["values"]
        status = prop["status"]
        prop_name = prop["key"]
        children = stylish(values, level + 1) if isinstance(values, list)\
            else None

        result += f'{INDENT * (level * 2 - 1)}'

        if status != CHANGED:
            result += handle_none_pristine(prop_name, status, values, children)
        else:
            if children:
                result += f'{JSON_PREFIX[PRISTINE]}' \
                          f'{prop["key"]}: {children}'
            else:
                initial_children = stylish(values["initial"], level + 1)\
                    if isinstance(values["initial"], list) \
                    else None
                current_children = stylish(values["current"], level + 1)\
                    if isinstance(values["current"], list) \
                    else None

                result += handle_none_pristine(
                    prop_name,
                    DELETED,
                    values,
                    initial_children
                ) + f'\n{INDENT * (level * 2 - 1)}'

                result += handle_none_pristine(
                    prop_name,
                    ADDED,
                    values,
                    current_children
                )
        result += '\n'

    result += f'{INDENT * (level - 1) * 2}{"}"}'

    return result.replace(": False", ": false")\
        .replace(": True", ": true")\
        .replace(": None", ": null")
