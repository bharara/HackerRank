t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    pr = 2
    large = 0

    while pr * pr <= n:
        if n%pr == 0:
            n //= pr
            large = pr
        else:
            pr += 1

    if n > large:
        large = n

    print(large)
