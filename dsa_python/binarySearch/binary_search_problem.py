################### PROBLEM 1 #######################
"""
    When I try to find number 50 in below list using binary search, it doesn't work and returns me -1 index. Why is that?
    array = [7, 10, 17, 3, 1, 20, 50, 45, 37]
"""
#  Answer: It is because the list is not sorted. Binary search requires the list to be sorted.

################### PROBLEM 2 #######################
"""
    Find index of all the occurence of a number from sorted list
    array = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    target = 15
"""
# Solution 
"""
    It tries to find an index of a number using binary search. Now since the list is sorted,
    it can do left and right scan from the initial index to find all occurances of a given element.
"""
"""
    This method is not most efficient and I want you to figure out even a better way of doing it. In
    any case below method is still effective
"""

from binary_search import binary_search

def occurence_indices(array, target):
    """
    Prints the indices of all occurrences of `target` in `array`.
    """
    index = binary_search(array, target)
    
    if index == -1:
        print(f"{target} not found in array {array}.")
        return

    indices = [index]
    left, right = index - 1, index + 1

    while left >= 0:
        if array[left] == target:
            indices.append(left)
            left -= 1
        else:
            break

    while right < len(array):
        if array[right] == target:
            indices.append(right)
            right += 1
        else:
            break

    return sorted(indices)


# This returns the count of occurence of the target in the given array
def count_occurrences(array, target):
    """
    Counts the number of occurrences of `target` in `array`.
    """
    index = binary_search(array, target)

    if index == -1:
        return 0

    count = 1
    left, right = index - 1, index + 1

    while left >= 0 and array[left] == target:
        count += 1
        left -= 1

    while right < len(array) and array[right] == target:
        count += 1
        right += 1

    return count

def binary_search_first(array, target):
    """
    Returns the index of the first occurrence of `target` in `array`,
    or -1 if `target` is not found.
    """
    left, right = 0, len(array) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            result = mid
            right = mid - 1
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def binary_search_last(array, target):
    """
    Returns the index of the last occurrence of `target` in `arr`,
    or -1 if `target` is not found.
    """
    left, right = 0, len(array) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            result = mid
            left = mid + 1
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def count_occurrence(arr, target):
    """
    Counts the number of occurrences of `target` in `arr`.
    """
    first_index = binary_search_first(arr, target)
    last_index = binary_search_last(arr, target)

    if first_index == -1 or last_index == -1:
        return -1

    return last_index - first_index + 1


if __name__ == '__main__':
    array = [1,4,6,9,11,13,14,15,15,15,17,21,34,34,37,56,70]
    target = 15
    indices = occurence_indices(array=array, target=target)
    count1 = count_occurrences(array=array,target=target)
    count2 = count_occurrences(array, target)


    print(f"Indices of occurence of {target} are {indices}")
    print(f"Count of occurence of {target} is {count1}")
    print(f"{target} occurs {count2} times in the array.")