def longest_subarray_sum_k(nums, k):
    prefix_sum_map = {}
    current_sum = 0
    max_length = 0

    for i in range(len(nums)):
        current_sum += nums[i]

        if current_sum == k:
            max_length = i + 1

        if (current_sum - k) in prefix_sum_map:
            max_length = max(max_length, i - prefix_sum_map[current_sum - k])

        if current_sum not in prefix_sum_map:
            prefix_sum_map[current_sum] = i

    return max_length


# Example usage
nums = [10, 5, 2, 7, 1, 9]
k = 15
print("Longest Subarray Length:", longest_subarray_sum_k(nums, k))
