t = int(input())

for t0 in range(t):

    m = (int(input())-1)//2
    s = ((16*(m**3)+26*m)//3)+((10*(m**2))+1)
    print(int(s%1000000007))