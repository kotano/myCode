class Counter(object):
    """A simple integral counter."""

    def __init__(self):
        """Initialize a new counter with zero as starting value."""
        self.value = 0

    def inc(self, amount=1):
        """Increment counter's value."""
        self.value = max(self.value + amount, 0)

    def dec(self, amount=1):
        """Decrement counter's value."""
        self.inc(-amount)


# BEGIN (write your solution here)
class LimitedCounter(Counter):
    def __init__(self, limit):
        super().__init__()
        self.limit = limit

    def inc(self, amount=1):
        if self.value < self.limit:
            super().inc(amount)
        if self.value > self.limit:
            self.value = self.limit

# END

# # BEGIN MASTER
# class LimitedCounter(Counter):
#     """A counter with limited maximal value."""

#     def __init__(self, limit):
#         """Initialize a new counter with some limit."""
#         self.limit = limit
#         self._actual_value = 0
#         super().__init__()

#     @property
#     def value(self):
#         return self._actual_value

#     @value.setter
#     def value(self, new_value):
#         self._actual_value = min(new_value, self.limit)
# # END

def test_counter():
    counter = Counter()
    counter.inc()
    counter.inc(7)
    assert counter.value == 8
    counter.dec(10)
    assert counter.value == 0
    counter.inc(7)
    counter.inc(7)
    assert counter.value == 14


def test_limitedcounter():
    counter = LimitedCounter(limit=10)
    counter.inc()
    counter.inc(7)
    assert counter.value == 8
    counter.dec(10)
    assert counter.value == 0
    counter.inc(7)
    counter.inc(7)
    assert counter.value == 10

if __name__ == "__main__":
    test_counter()
    test_limitedcounter()
