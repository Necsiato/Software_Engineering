def remove_fun(tup, elem):
    if elem in tup:
        tup_list = list(tup)
        tup_list.remove(elem)
        return tuple(tup_list)
    else:
        return tup
print(remove_fun((1, 2, 3), 1))
print(remove_fun((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(remove_fun((2, 4, 6, 6, 4, 2), 9))

