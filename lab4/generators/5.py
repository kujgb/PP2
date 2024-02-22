def down(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input())
down = down(n)
for i in down:
    print(i)