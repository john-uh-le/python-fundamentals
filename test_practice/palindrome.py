def is_palindrome(s):
    """
    A palindrome reads the same forward and backward.

    Examples:

    "racecar" → True
    "level"   → True
    "cloud"   → False
    """
    right = len(s) -1
    left = 0
    while left < right:
        if s[left] != s[right]:
            return False
        left = left + 1
        right = right - 1
    return True

print(is_palindrome("car"))
print(is_palindrome("otto"))
print(is_palindrome("level"))