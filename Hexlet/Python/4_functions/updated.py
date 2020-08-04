def updated(dictionary, **kwargs):
    res = dictionary.copy()
    if kwargs:
        res.update(kwargs)
    return res


# BEGIN
def m_updated(dictionary, **kwargs):
    new = dictionary.copy()
    new.update(kwargs)
    return new
# END
