from binary_search import linear_search, binary_search, binary_search_recursive

if __name__ == '__main__':
    numbers_list = [7, 10, 17, 3, 1, 20, 50, 45, 37]
    number_to_find = 45

    print(f"The numbers list is: {numbers_list}")
    numbers_list_sorted = sorted(numbers_list)
    print(f"The sorted numbers list is: {numbers_list_sorted}")

    idx_linear = linear_search(numbers_list_sorted, number_to_find)
    idx_binary = binary_search(numbers_list_sorted, number_to_find)
    idx_binary_rec = binary_search_recursive(numbers_list_sorted, number_to_find, 0, len(numbers_list))

    print(f"Number found at index {idx_linear} using linear search")
    print(f"Number found at index {idx_binary} using binary search")
    print(f"Number found at index {idx_binary_rec} using binary search recursive")
    