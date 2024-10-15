def find_subtuple(tpl, elem):
    if elem not in tpl:
        return ()
    first_occurrence = tpl.index(elem)
    sub_tpl = tpl[first_occurrence:]
    if elem in sub_tpl[1:]:
        second_occurrence = sub_tpl[1:].index(elem) + 1
        return sub_tpl[:second_occurrence + 1]
    return sub_tpl
print(find_subtuple((1, 2, 3), 8))
print(find_subtuple((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(find_subtuple((1, 2, 8, 5, 1, 2, 9), 8))
