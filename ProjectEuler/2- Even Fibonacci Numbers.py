t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    x = 0
    y = 1

    s = 0

    while x <= n:
        if x%2 == 0:
            s += x

        x, y = y, x+y

    print(s)
