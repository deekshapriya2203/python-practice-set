def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        # Find the smallest element in remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example
arr = [64, 25, 12, 22, 11]
print("Sorted array:", selection_sort(arr))
