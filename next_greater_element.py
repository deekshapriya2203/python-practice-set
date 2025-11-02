def next_greater_elements(nums):
    n = len(nums)
    result = [-1] * n
    stack = []

    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        
        if stack:
            result[i] = stack[-1]
        
        stack.append(nums[i])
    
    return result

# Example usage
nums = [4, 5, 2, 10, 8]
print("Next Greater Elements:", next_greater_elements(nums))
