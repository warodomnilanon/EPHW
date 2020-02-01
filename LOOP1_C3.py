import sys
a = 0
while a < 10:
    b = 1
    while b <= a:
        sys.stdout.write("x")
        b += 1
    print()
    a += 1