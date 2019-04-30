import math
def divSum(n) :
    if n==1:
        return 1

    result = 0
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if (n % i == 0): 
            if (i == (n/i)) : 
                result += i 
            else : 
                result += i + n//i 
        
    if n**2==n:
        result += n          
    return (result + 1)

def isSum (n):      
    for i in lst:
        if i > n:
            return False
        if (n-i) in lst:
            return True
        return False

lst = set(x for x in range(12, 28123) if (divSum(x) > x))

t = int(input())
for t0 in range(t):
    n = int(input())

    if isSum(n):
        print("YES")
    else:
        print("NO")