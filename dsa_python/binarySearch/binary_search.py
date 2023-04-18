from util import time_it

@time_it
def linear_search(array, target):
    for idx, element in enumerate(array):
        if element == target:
            return idx
    return -1

@time_it
def binary_search(array,target):
    left_idx = 0
    right_idx = len(array) - 1
    mid_idx = 0

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        mid_element = array[mid_idx]

        if mid_element == target:
            return mid_idx
        elif mid_element < target:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1

    return -1
    

@time_it
def binary_search_recursive(array, target, left_idx, right_idx):
    if right_idx < left_idx:
        return -1

    mid_idx = (left_idx + right_idx) // 2
    if mid_idx >= len(array) or mid_idx < 0:
        return -1

    mid_element = array[mid_idx]

    if mid_element == target:
        return mid_idx
    elif mid_element < target:
        left_idx = mid_idx + 1
    else:
        right_idx = mid_idx - 1

    return binary_search_recursive(array, target, left_idx, right_idx)