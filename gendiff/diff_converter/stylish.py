from gendiff.consts import JSON_PREFIX, INDENT, PROPERTY_STATUS,\
    STATUS_VALUES_RELATION


def handle_none_pristine(name, status, value, children):
    name_str = f'{JSON_PREFIX[status]}{name}:'
    prop_str = f' {children or value[STATUS_VALUES_RELATION[status]]}'
    return f'{name_str}{prop_str}'


def stylish(diff, level=1):
    result = "{\n"

    for prop in diff:
        values = prop["values"]
        status = prop["status"]
        prop_name = prop["name"]
        children = stylish(values, level + 1) if isinstance(values, list)\
            else None

        result += f'{INDENT * (level * 2 - 1)}'

        if status != PROPERTY_STATUS.CHANGED:
            result += handle_none_pristine(prop_name, status, values, children)
        else:
            if children:
                result += f'{JSON_PREFIX[PROPERTY_STATUS.PRISTINE]}' \
                          f'{prop["name"]}: {children}'
            else:
                initial_children = stylish(values["initial"], level + 1)\
                    if isinstance(values["initial"], list) \
                    else None
                current_children = stylish(values["current"], level + 1)\
                    if isinstance(values["current"], list) \
                    else None

                result += handle_none_pristine(
                    prop_name,
                    PROPERTY_STATUS.DELETED,
                    values,
                    initial_children
                ) + f'\n{INDENT * (level * 2 - 1)}'

                result += handle_none_pristine(
                    prop_name,
                    PROPERTY_STATUS.ADDED,
                    values,
                    current_children
                )
        result += '\n'

    result += f'{INDENT * (level - 1) * 2}{"}"}'

    return result.replace(": False", ": false")\
        .replace(": True", ": true")\
        .replace(": None", ": null")
