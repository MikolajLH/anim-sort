

def selection_sort(array, comp):
    for i in range(len(array)):
        k = i
        for j in range(i, len(array)):
            yield j
            if comp(array[j], array[k]):
                k = j
        yield k
        yield i
        array[k], array[i] = array[i], array[k]
    yield 0