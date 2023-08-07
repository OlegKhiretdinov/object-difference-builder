"""
dif_example = [
    {
        name: 'prop_1',
        status: 'dont_change' | 'changed' | 'delete' | 'added'
        # if status == 'dont_change'
        values: {initial: 'a'}
        # if status == 'changed'
        values: {initial: 'a', current: 'b'}
        # if status == 'added'
        values: {current: 'c'}
        # if status == 'delete'
        values: {initial: 'a'}

        # if prop is object
        values: []
    },
    {
        name: 'prop_2'
        ...
    }
]
"""


def get_changed_values(name, dict_1, dict_2):
    is_prop_1_dict = isinstance(dict_1[name], dict)
    is_prop_2_dict = isinstance(dict_2[name], dict)

    # оба свойства строки
    values = {
        "initial": dict_1[name],
        "current": dict_2[name]
    }

    if is_prop_1_dict and is_prop_2_dict:
        values = get_dict_diff(dict_1[name], dict_2[name])
    elif is_prop_1_dict and not is_prop_2_dict:
        values = {
            "initial": get_dict_diff(dict_1[name], dict_1[name]),
            "current": dict_2[name]
        }
    elif not is_prop_1_dict and is_prop_2_dict:
        values = {
            "initial": dict_1[name],
            "current": get_dict_diff(dict_2[name], dict_2[name])
        }

    return values


def get_dict_diff(dict_1, dict_2):
    keys1 = list(dict_1)
    keys2 = list(dict_2)
    keys1.sort()
    keys2.sort()
    dict_dif = []

    for key in keys1:
        prop_desc = {"key": key}
        if key not in keys2:
            prop_desc["status"] = "deleted"
            prop_desc["values"] = get_dict_diff(dict_1[key], dict_1[key])\
                if isinstance(dict_1[key], dict)\
                else {"initial": dict_1[key]}
        elif dict_1[key] == dict_2[key]:
            prop_desc["status"] = "pristine"
            prop_desc["values"] = get_dict_diff(dict_1[key], dict_2[key])\
                if isinstance(dict_1[key], dict)\
                else {"initial": dict_1[key]}
        else:
            prop_desc["status"] = "changed"
            prop_desc["values"] = get_changed_values(key, dict_1, dict_2)

        dict_dif.append(prop_desc)

    for key in keys2:
        if key not in keys1:
            prop_desc = {"key": key}
            prop_desc["status"] = "added"
            prop_desc["values"] = get_dict_diff(dict_2[key], dict_2[key])\
                if isinstance(dict_2[key], dict)\
                else {"current": dict_2[key]}
            dict_dif.append(prop_desc)

    dict_dif.sort(key=lambda item: item["key"])

    return dict_dif
