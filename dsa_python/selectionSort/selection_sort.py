def selection_sort(arr):
    """
    Returns the sorted `arr`.
    """
    n = len(arr)
    for i in range(n-1):
        # Find the minimum element in the unsorted part of the array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the minimum element with the first element in the unsorted part of the array
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr