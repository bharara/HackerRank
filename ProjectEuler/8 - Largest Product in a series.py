def product (l):
    m = 1
    for v in l:
        m *= int(v)
    return m


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()

    large = 0

    for i in range (n-k+1):
        val = product (list (str (num) [ i : i+k ]))
        if large < val:
            large = val

    print (large)
