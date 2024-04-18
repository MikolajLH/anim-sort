def shell_sort(array, comp):
    h = 1
    for h in range(len(array)):
        h = 3 * h + 1
    h //= 9
    if h == 0:
        h = 1
    while h > 0:
        for j in range(len(array) - h - 1,-1,-1):
            key = array[j]
            i = j + h
            while i < len(array) and comp(array[i], key):
                yield i
                array[i - h] = array[i]
                i += h
            array[i - h] = key
        h //= 3
    yield 0