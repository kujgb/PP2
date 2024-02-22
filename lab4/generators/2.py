n = int(input())
def generate_even(n):
    for i in range(0, n+1, 2):
            yield i
even = generate_even(n)
print(*even, sep=", ")