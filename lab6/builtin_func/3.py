def palindrome(s):
    return s == s[::-1]

s = str(input())
res = palindrome(s)
if res:
    print("Yes")
else:
    print("No")