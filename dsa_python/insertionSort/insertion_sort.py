def insertion_sort(arr):
    n = len(arr)
    # Traverse through the array starting from the second element
    for i in range(1, n):
        # Store the current element in a variable
        key = arr[i]
        # Initialize a pointer to the previous element
        j = i - 1
        # Move the pointer backwards and swap elements until
        # the current element is in its correct position
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        # Insert the current element in its correct position
        arr[j+1] = key
    # Return the sorted array
    return arr