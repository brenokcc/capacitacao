
def match_keys(data, valid, path):
    data_keys = data.keys()
    valid_keys = valid.keys()
    extra_keys = data_keys - valid_keys
    missing_keys = valid_keys - data_keys
    if missing_keys or extra_keys:
        msg = []
        if missing_keys:
            msg.append('missing keys:')
            msg.append(','.join({'{}.{}'.format(path, str(key)) for key in missing_keys}))
        if extra_keys:
            msg.append('extra keys:')
            msg.append(','.join({'{}.{}'.format(path, str(key)) for key in extra_keys}))
        return False, ' '.join(msg)
    else:
        return True, None


def match_types(data, template, path):
    for key, value in template.items():
        if isinstance(value, dict):
            template_type = dict
        else:
            template_type = value
        data_value = data.get(key, object())
        if not isinstance(data_value, template_type):
            msg = list()
            msg.append('incorrect type:')
            msg.append('{}.{}'.format(path, key))
            msg.append('-> expected {}, found {}'.format(template_type.__name__, type(data_value).__name__))
            return False, ' '.join(msg)
    return True, None


def recurse_validate(data, template, path):
    is_valid, msg = match_keys(data, template, path)
    if not is_valid:
        return False, msg

    is_valid, msg = match_types(data, template, path)
    if not is_valid:
        return False, msg

    dictionary_type_keys = {key for key, value in template.items() if isinstance(value, dict)}
    for key in dictionary_type_keys:
        sub_path = path + '.' + str(key)
        sub_template = template[key]
        sub_data = data[key]
        is_valid, msg = recurse_validate(sub_data, sub_template, sub_path)
        if not is_valid:
            return False, msg

    return True, None
