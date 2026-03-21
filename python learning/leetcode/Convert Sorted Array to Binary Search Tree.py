def sorted_array_to_bst(nums):
    if not nums:
        return None

    mid = len(nums) // 2
    root = {
        "val": nums[mid],
        "left": sorted_array_to_bst(nums[:mid]),
        "right": sorted_array_to_bst(nums[mid+1:])
    }

    return root

# Example usage:
nums = [-10, -3, 0, 5, 9]
tree = sorted_array_to_bst(nums)
print(tree)
