def mySqrt(x: int) -> int:
    if x < 2:
        return x
    
    left, right = 2, x // 2
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right
print(mySqrt(8))  # Output: 2
