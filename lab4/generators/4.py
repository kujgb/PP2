x = int(input())
y = int(input())

def squares(x, y):
    for i in range(x, y + 1):
        yield i ** 2
for i in squares(x, y):
    print(i)