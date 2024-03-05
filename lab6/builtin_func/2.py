def upper_lower_num():
    s = str(input())
    upper = 0
    lower = 0
    for char in s:
       if char.islower():
        lower += 1
       elif char.isupper():
        upper += 1
    print(f"Uppercase count: {upper}")
    print(f"Lowercade count: {lower}")

upper_lower_num()