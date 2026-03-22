def is_palindrome(x):
    if x < 0:
        return False
    
    s = str(x)
    return s == s[::-1]

num_str = input("Enter a number: ")

num = int(num_str)

if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
