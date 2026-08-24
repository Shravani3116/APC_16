def check_palindrome(s):
    return s == s[::-1]

print(check_palindrome("racecar"))
print(check_palindrome("hello"))