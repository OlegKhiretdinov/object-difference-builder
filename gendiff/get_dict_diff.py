def get_dict_diff(dict_1, dict_2):
    result = "{\n"
    keys1 = list(dict_1)
    keys2 = list(dict_2)
    keys1.sort()
    keys2.sort()

    for i in keys1:
        if i not in keys2:
            result += f'  - {i}: {dict_1[i]}\n'
        elif dict_1[i] == dict_2[i]:
            result += f'    {i}: {dict_1[i]}\n'
        else:
            result += f'  - {i}: {dict_1[i]}\n'
            result += f'  + {i}: {dict_2[i]}\n'

    for i in keys2:
        if i not in keys1:
            result += f'  + {i}: {dict_2[i]}\n'

    result += "}"

    return result
