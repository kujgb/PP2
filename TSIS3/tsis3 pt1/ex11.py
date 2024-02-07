def a(str1):
    str2 = str1[::-1]
    if str1 == str2:
        return "Palindrome"
    return " Not palindrome"
str1 = str(input())
print(a(str1))