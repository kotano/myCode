def apply_diff(target, diff):
    to_add = diff.get('add', None)
    to_rem = diff.get('remove', None)

    if to_add:
        target.update(to_add)
    if to_rem:
        target.difference_update(to_rem)


def upd_apply_diff(target, diff):
    target.update(diff.get('add', {}))
    target.difference_update(diff.get('remove', {}))


# MASTER BEGIN
def m_apply_diff(set_for_update, diff):
    for k, v in diff.items():
        if k == 'add':
            set_for_update.update(v)
        elif k == 'remove':
            set_for_update.difference_update(v)
# END
