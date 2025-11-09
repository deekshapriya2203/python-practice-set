import heapq

def kth_largest(arr, k):
    # Use heapq.nlargest to get k largest elements
    return heapq.nlargest(k, arr)[-1]

# Example
arr = [3, 2, 1, 5, 6, 4]
k = 2
print(f"The {k}th largest element is {kth_largest(arr, k)}")
