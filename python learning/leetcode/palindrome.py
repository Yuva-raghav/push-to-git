def is_palindrome(x):
    # Negative numbers are not palindromes
    if x < 0:
        return False
    
    # Convert number to string and check if it reads the same backwards
    s = str(x)
    return s == s[::-1]

# Get input from user
num_str = input("Enter a number: ")

# Convert to integer
num = int(num_str)

# Check if it's a palindrome
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
