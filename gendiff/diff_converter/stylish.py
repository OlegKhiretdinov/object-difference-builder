from gendiff.consts import JSON_DIFF_PREFIX, INDENT, PROPERTY_STATUS


def stylish(diff, level=1):
    result = "{\n"

    for prop in diff:
        values = prop["values"]
        children = stylish(values, level + 1) if isinstance(values, list)\
            else None

        result += f'{INDENT * (level * 2 - 1)}'

        if prop["status"] == PROPERTY_STATUS.ADDED:
            result += f'{JSON_DIFF_PREFIX.ADD}' \
                      f'{prop["name"]}: {children or values["current"]}'
        elif prop["status"] == PROPERTY_STATUS.DELETED:
            result += f'{JSON_DIFF_PREFIX.DELETE}' \
                      f'{prop["name"]}: {children or values["initial"]}'
        elif prop["status"] == PROPERTY_STATUS.PRISTINE:
            result += f'{JSON_DIFF_PREFIX.PRISTINE}' \
                      f'{prop["name"]}: {children or values["initial"]}'
        elif prop["status"] == PROPERTY_STATUS.CHANGED:
            if children:
                result += f'{JSON_DIFF_PREFIX.PRISTINE}' \
                          f'{prop["name"]}: {children}'
            else:
                initial = stylish(values["initial"], level + 1)\
                    if isinstance(values["initial"], list) \
                    else values["initial"]
                current = stylish(values["current"], level + 1)\
                    if isinstance(values["current"], list) \
                    else values["current"]

                result += f'{JSON_DIFF_PREFIX.DELETE}{prop["name"]}: ' \
                          f'{initial }\n'
                result += f'{INDENT * (level * 2 - 1)}{JSON_DIFF_PREFIX.ADD}' \
                          f'{prop["name"]}: {current}'
        result += '\n'

    result += f'{INDENT * (level - 1) * 2}{"}"}'

    asd = result.replace(": False", ": false")\
        .replace(": True", ": true")\
        .replace(": None", ": null")

    return asd
