def factorial(n):
    if n == 0:
        return 1
    return n * factorial (n - 1)


t = int(input())
for t0 in range(t):
    n = int(input())

    s = 0
    for i in list(str(factorial(n))):
        s += int(i)

    print(s)
