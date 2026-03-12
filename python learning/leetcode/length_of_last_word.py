def lengthOfLastWord(s: str) -> int:
    words = s.strip().split()
    return len(words[-1]) if words else 0


# Example usage:
print(lengthOfLastWord("Hello World"))       # Output: 5
print(lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
print(lengthOfLastWord("luffy is still joyboy"))        # Output: 6
