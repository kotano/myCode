def toggle(flags, sets):
    if flags in sets:
        sets.remove(flags)
    elif flags not in sets:
        sets.add(flags)


def toggled(flags, sets):
    new_sets = sets.copy()
    toggle(flags, new_sets)
    return new_sets
