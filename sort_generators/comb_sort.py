


def comb_sort(array, comp):
    gap, swapped = len(array), True
    while gap > 1 or swapped:
        gap = (gap * 10) // 13
        if gap == 0: gap = 1
        swapped = False
        i = 0
        while i + gap < len(array):
            yield i
            if comp(array[gap + i], array[i]):
                array[i], array[gap + i] = array[gap + i], array[i]
                swapped = True
            i += 1
    yield 0