import sys
a = 0
while a < 10:
    b = 0
    while b <= 9-a:
        sys.stdout.write("x")
        b += 1
    print()
    a += 1
