def nsum(n, p):
    a = n
    ns = 0
    while n > 0:
        ns += (n%10)** p
        n //= 10
    return ns == a


p = int(input())
n = 1000000
tot = 0
for i in range(2, n):
    if nsum(i, p):
        tot += i

print(tot)
