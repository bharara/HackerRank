from math import floor, ceil

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    large = -1
    for a in range(1, n//2):
        ##   B = (N-A) – A2 / 2(N-A)
        temp = n - a
        b = temp/2 - (a*a) / (2 * temp)
        if floor(b) == ceil(b):
            val = a * b * (n - a - b)
            if val > large:
                large = int(val)

    print(large)