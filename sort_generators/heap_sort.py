
def heap_sort(array, comp):
    def left(i): return 2*i + 1
    def right(i): return 2*i + 2
    def parent(i): return (i-1)//2

    def heapify(array, n, i, comp):
        L = left(i)
        R = right(i)
        max_ind = i
        if L < n and not comp(array[L], array[max_ind]):
            max_ind = L
        if R < n and not comp(array[R], array[max_ind]):
            max_ind = R
        if max_ind != i:
            yield max_ind
            array[max_ind], array[i] = array[i], array[max_ind]
            yield from heapify(array, n, max_ind, comp)
    
    def build_heap(array, comp):
        n = len(array)
        for i in range(parent(n-1),-1,-1):
            yield from heapify(array, n, i, comp)

    n = len(array)
    yield from build_heap(array, comp)
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        yield from heapify(array, i, 0, comp)
    yield 0