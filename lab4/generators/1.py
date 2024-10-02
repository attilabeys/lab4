def squares(n):
    for i in range(1, n + 1):
        yield i ** 2
N = int(input())
generator = squares(N)
for g in generator:
    print(g)