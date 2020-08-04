def greet(name, *args):
    result = [name]
    for x in args:
        result.append(' and '+x)
    return 'Hello, {}!'.format(''.join(result))


# BEGIN
def m_greet(who, *args):
    names = ' and '.join((who,) + args)
    return 'Hello, {}!'.format(names)
# END
