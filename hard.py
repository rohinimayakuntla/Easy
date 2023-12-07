def shortestPalindrome(s):
    if not s:
        return ""
    i = 0
    for j in range(len(s) - 1, -1, -1):
        if s[i] == s[j]:
            i += 1
    if i == len(s):
        return s
    remaining = s[i:]
    return remaining[::-1] + shortestPalindrome(s[:i]) + remaining
s = input("Enter the string: ")
result = shortestPalindrome(s)
print("Output:", result)
