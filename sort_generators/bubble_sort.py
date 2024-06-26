

def bubble_sort(array, comp):
    for i in range(len(array) - 1):
        comparisions = False
        for j in range(len(array) - 1 - i):
            yield j
            if comp(array[j + 1], array[j]):
                comparisions = True
                yield j + 1
                array[j], array[j + 1] = array[j + 1], array[j]
                
        if comparisions is False:
            break
    yield 0