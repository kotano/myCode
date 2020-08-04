def make_module(step=1):
    return {
        'inc': lambda x: x + step,
        'dec': lambda x: x - step,
    }
