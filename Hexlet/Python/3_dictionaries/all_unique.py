# def all_unique_sets(iterator):
def all_unique(iterable):
    items = list(iterable)
    print(len(items))
    print(len(set(items)))
    return len(set(items)) == len(items)


print(all_unique(iter([])),)
print(all_unique(iter([1])))
print(all_unique([]))
print(all_unique("cat"))
print(all_unique("lol"))
