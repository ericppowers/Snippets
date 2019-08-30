def return_index(lst, index):
    if len(lst) <= index:
        return lst
    else:
        return lst[index]


def double_index(lst, index):
    if len(lst) <= index:
        return lst
    else:
        lst[index] *= 2
        return lst

