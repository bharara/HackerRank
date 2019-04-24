t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    s1 = n*(n+1)/2
    s1 *= s1
    s2 = n*(n+1)*(2*n+1)/6

    print(int(abs(s1-s2)))