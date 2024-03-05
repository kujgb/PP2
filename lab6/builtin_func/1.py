def multiply(num):
    total = 1
    for x in num:
        total *= x
        return total
num = list(map(int, input("Enter nums without spaces: ").split(',')))
result = multiply(num)
print("The product of element equals:", result)