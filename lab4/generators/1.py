def squares(N):
    for i in range(1, N + 1):
        yield i * i

for x in squares(int(input())):
    print(x)