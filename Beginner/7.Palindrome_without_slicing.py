'''
Problem:
Given a string s, determine whether it is a palindrome or not.
A palindrome is a string that reads the same forward and backward — for example, "madam" or "racecar".
You must solve this without using string slicing (i.e., no s[::-1]).

String length: 1 ≤ len(s) ≤ 10^5

Should be case-insensitive.

Ignore spaces and non-alphanumeric characters if specified (optional enhancement).

'''

def check_palindrome(s: str):
    s = s.lower()
    start = 0
    end = len(s) - 1
    while start <= end:
        # Skip non-alphanumeric characters at the start
        if not s[start].isalnum():
            start += 1
        # Skip non-alphanumeric characters at the end
        elif not s[end].isalnum():
            end -= 1
        # Compare characters
        elif s[start] != s[end]:
            return False
        else:
            start += 1
            end -= 1
    return True

if __name__ == '__main__':
    s = "level"
    result = check_palindrome(s)
    if result:
        print(f"The string '{s}' is a Palindrome!")
    else:
        print(f"The string '{s}' is not a Palindrome!")