def substract(num):
    while num >= 0:
        yield num
        num -= 1

N = int(input())
gen = substract(N)
for i in gen:
    print(i)