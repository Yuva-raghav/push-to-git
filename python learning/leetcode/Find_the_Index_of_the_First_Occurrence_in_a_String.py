def str_str(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

# Example usage
print(str_str("sadbutsad", "sad"))  # Output: 0
print(str_str("leetcode", "leeto")) # Output: -1
