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

from gendiff.consts import PROPERTY_STATUS


def get_dict_diff(dict_1, dict_2):
    keys1 = list(dict_1)
    keys2 = list(dict_2)
    keys1.sort()
    keys2.sort()
    dict_dif = []

    for i in keys1:
        prop_description = {"name": i}
        if i not in keys2:
            prop_description["status"] = PROPERTY_STATUS.DELETED
            prop_description["values"] = get_dict_diff(dict_1[i], dict_1[i])\
                if isinstance(dict_1[i], dict)\
                else {"initial": dict_1[i]}
        elif dict_1[i] == dict_2[i]:
            prop_description["status"] = PROPERTY_STATUS.PRISTINE
            prop_description["values"] = get_dict_diff(dict_1[i], dict_2[i])\
                if isinstance(dict_1[i], dict)\
                else {"initial": dict_1[i]}
        else:
            prop_description["status"] = PROPERTY_STATUS.CHANGED
            is_prop_1_dict = isinstance(dict_1[i], dict)
            is_prop_2_dict = isinstance(dict_2[i], dict)

            # оба свойства строки
            values = {
                "initial": dict_1[i],
                "current": dict_2[i]
            }
            if is_prop_1_dict and is_prop_2_dict:
                values = get_dict_diff(dict_1[i], dict_2[i])
            elif is_prop_1_dict and not is_prop_2_dict:
                values = {
                    "initial": get_dict_diff(dict_1[i], dict_1[i]),
                    "current": dict_2[i]
                }
            elif not is_prop_2_dict and is_prop_2_dict:
                values = {
                    "initial": dict_1[i],
                    "current": get_dict_diff(dict_2[i], dict_2[i])
                }

            prop_description["values"] = values

        dict_dif.append(prop_description)

    for i in keys2:
        if i not in keys1:
            prop_description = {"name": i}
            prop_description["status"] = PROPERTY_STATUS.ADDED
            prop_description["values"] = get_dict_diff(dict_2[i], dict_2[i])\
                if isinstance(dict_2[i], dict)\
                else {"current": dict_2[i]}
            dict_dif.append(prop_description)

    dict_dif.sort(key=lambda item: item["name"])

    return dict_dif
