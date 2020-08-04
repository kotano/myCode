class Counter(object):
    value = int()

    def inc(self, delta=1):
        self.value = self.value + delta  # noqa WPS601

    def dec(self, delta=1):
        self.value = self.value - delta  # noqa WPS601


# class Counter:  # noqa: WPS306
#     value = 0

#     def inc(self, delta=1):
#         self.value = max(self.value + delta, 0)  # noqa: WPS601

#     def dec(self, delta=1):
#         self.inc(-delta)
