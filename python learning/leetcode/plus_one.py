def plusOne(digits: list[int]) -> list[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    
    return [1] + digits


# Example usage:
print(plusOne([1,2,3]))   # Output: [1,2,4]
print(plusOne([9,9,9]))   # Output: [1,0,0,0]
