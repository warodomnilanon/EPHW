import sys
a = 0
while a < 10:
    b = 0
    while b <= 8-a:
        sys.stdout.write("-")
        b += 1
    c = 0
    while c <= a:
        sys.stdout.write("x")
        c += 1
    print()
    a += 1



