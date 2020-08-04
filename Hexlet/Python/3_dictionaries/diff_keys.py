def diff_keys(old, new):
    old_keys, new_keys = set(old.keys()), set(new.keys())
    return {
        'kept': new_keys & old_keys,
        'added': (new_keys - old_keys),
        'removed': old_keys - new_keys,
    }
