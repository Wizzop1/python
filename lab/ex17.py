def isPalindrome(s):
    if s == s[::-1]:
        return 1
    return 0
print(isPalindrome(input()))