# def duplicate(lst):
#     print(id(lst), 'before')
#     copy = lst[:]
#     for x in copy:
#         lst.append(x)
#     print(id(lst), 'changed')


# master
def duplicate(lst):
    lst.extend(lst)


todup = [1, 2]
print(id(todup), 'first')
duplicate(todup)
print(todup)
print(id(todup), 'last')
