def even(n):
    for i in range(0, n + 1):
        if i % 3 == 0:
         if i % 4 == 0:
          yield i
N = int(input())
generator = even(N)
for g in generator:
    print(g, end=", ")