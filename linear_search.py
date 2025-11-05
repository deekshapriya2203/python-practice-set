def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i  # Return the index
    return -1  # Element not found

# Example
arr = [10, 25, 30, 45, 50]
key = 45
result = linear_search(arr, key)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
