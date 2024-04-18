from copy import copy


def merge_sort(array, comp):
    def merge(array, low, mid, high, comp):    
        left = copy(array[low:mid])
        right = copy(array[mid:high])

        left_i, right_i, merged_i = 0, 0, low
        while left_i < len(left) and right_i < len(right):
            yield merged_i
            if comp(left[left_i], right[right_i]):
                array[merged_i] = left[left_i]
                left_i += 1
            else:
                array[merged_i] = right[right_i]
                right_i += 1
            merged_i += 1

        while left_i < len(left):
            yield merged_i
            array[merged_i] = left[left_i]
            left_i += 1
            merged_i += 1
    
        while right_i < len(right):
            yield merged_i
            array[merged_i] = right[right_i]
            right_i += 1
            merged_i += 1

    def merge_sort_impl(array, low, high):
        if high - low >= 2:
            mid = (low + high) // 2
            yield from merge_sort_impl(array, low, mid)
            yield from merge_sort_impl(array, mid, high)
            yield from merge(array, low, mid, high, comp)

    yield from merge_sort_impl(array, 0, len(array))
    yield 0