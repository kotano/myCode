class Clock(object):
    def __init__(self, value=0):
        """Setting clock hour"""
        self.value = value

    @property
    def hours(self):
        return self.value % 12

    @hours.setter
    def hours(self, delta):
        self.value = delta

# # BEGIN
# class Clock:  # noqa: WPS306
#     def __init__(self):
#         """Create a new hour clock."""
#         self.hand_position = 0

#     @property
#     def hours(self):
#         return self.hand_position

#     @hours.setter
#     def hours(self, new_position):
#         self.hand_position = new_position % 12
# # END


def test_clock():
    clock = Clock()
    print(clock.hours == 0)
    clock.hours = clock.hours + 6
    print(clock.hours)
    clock.hours += 5
    print(clock.hours == 11)
    clock.hours += 4
    print(clock.hours == 3)
    clock.hours = clock.hours - 4
    print(clock.hours == 11)
    clock.hours = 123
    print(clock.hours == 3)


test_clock()
