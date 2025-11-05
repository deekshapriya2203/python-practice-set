def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps occurred, the array is already sorted
        if not swapped:
            break
    return arr

# Example
arr = [5, 3, 8, 4, 2]
print("Sorted array:", bubble_sort(arr))
