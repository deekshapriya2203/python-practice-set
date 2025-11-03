def second_largest(arr):
    if len(arr) < 2:
        return "Array too small"
    
    first = second = float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    return second if second != float('-inf') else "No second largest element"

# Example
arr = [10, 5, 20, 8, 20]
print("Second largest element:", second_largest(arr))
