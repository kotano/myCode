def call_twice(function, *args, **kwargs):
    res1 = function(*args, **kwargs)
    res2 = function(*args, **kwargs)
    return (res1, res2,)
# same as master
