from math import gcd

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    a = list(range(1,n+1))

    lcm = a[0]
    for i in a[1:]:
        lcm = int(lcm*i/gcd(lcm, i))
    print (lcm)
