def remove_element(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

# Example usage
nums = [3,2,2,3]
val = 3
length = remove_element(nums, val)
print("Length:", length)
print("Array after removal:", nums[:length])
