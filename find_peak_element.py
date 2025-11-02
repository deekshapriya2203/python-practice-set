def find_peak_element(nums):
    low, high = 0, len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return low  # or high, both point to the same index


# Example usage
nums = [1, 2, 1, 3, 5, 6, 4]
index = find_peak_element(nums)
print(f"Peak element is {nums[index]} at index {index}")
