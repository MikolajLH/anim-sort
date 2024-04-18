def insertion_sort(array, comp):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and comp(key, array[j]):
            yield j + 1
            yield j
            array[j + 1] = array[j]
            j -= 1
        yield j + 1
        array[j + 1] = key
    yield 0