


def quick_sort(array, comp):
    def partition(array, first, last, comp):
        pivot_index = last
        array[pivot_index], array[last] = array[last], array[pivot_index]

        i = first
        for k in range(first, last):
            yield k
            if comp(array[k], array[last]):
                array[k], array[i] = array[i], array[k]
                i += 1
        array[i], array[last] = array[last], array[i]
        yield i

    def quick_sort_impl(array, first, last, comp):
        if first < last:
            pivot_index = None
            for p in partition(array, first, last, comp):
                yield p
                pivot_index = p
            yield from quick_sort_impl(array, first, pivot_index - 1, comp)
            yield from quick_sort_impl(array, pivot_index + 1, last, comp)

    yield from quick_sort_impl(array, 0, len(array) - 1, comp)
    yield 0