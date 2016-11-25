def treat_key(key):
    if key.isnumeric():
        return int(key)
    return key


def treat_keys(keys):
    return [treat_key(key) for key in keys]
