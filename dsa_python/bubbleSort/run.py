from bubble_sort import bubble_sort

if __name__ == '__main__':
    # array = [7, 10, 17, 3, 1, 20, 50, 45, 37]
    array = ["mona", "dhaval", "aamir", "tina", "chang"]

    print(f"The unsorted array is: {array}")

    sorted_arr = bubble_sort(arr=array)

    print(f"The sorted array is {sorted_arr} after implementing bubble sort.")