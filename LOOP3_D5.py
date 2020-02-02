import math
n = int(input("n: "))
sum = 0
a = 1
while a <= n:
    sum += 1/a**a
    a += 1
print(math.sqrt(6 * (sum)))