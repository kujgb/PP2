def generator(n):
    for i in range(1, n):
        if i%3==0 and i%4==0:
            yield i
            
n = int(input())
div = generator(n)
for a in div:
    print(a)