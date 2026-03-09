# Function to find the positions of the two numbers
def two_sum(nums, target):
    for i in range(len(nums)): # Look at first number
        for j in range(i + 1, len(nums)): # Look at second number
            if nums[i] + nums[j] == target: # Check if they match the target
                return [i, j] # Return their positions

# 1. Ask user for a list of numbers
user_nums = input("Enter numbers separated by space: ")

# Convert the text into a list of integers
nums = [int(x) for x in user_nums.split()]

# 2. Ask user for the target number
user_target = int(input("Enter target number: "))

# 3. Call the function and print the result
output = two_sum(nums, user_target)
print("Output:", output)
