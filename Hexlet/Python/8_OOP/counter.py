class Counter(object):
    def __init__(self, value=0):
        """Create an immutable counter"""
        self.value = value

    def inc(self, delta=1):
        return Counter(max(self.value + delta, 0))

    def dec(self, delta=1):
        return self.inc(-delta)
