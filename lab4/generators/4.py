def squares(a, b):
 for i in range(a, b + 1):
    yield i ** 2

    
N1 = int(input())
N2 = int(input())
generator = squares(N1, N2)
for i in generator:
  print(i)