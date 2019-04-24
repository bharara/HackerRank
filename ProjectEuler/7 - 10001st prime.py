def isPrime(a):
    for i in range (3, int(a ** 0.5) + 1, 2):
        if a % i == 0:
            return False
    return True


prime = [0, 2, 3]
count  = 2

def getPrime (n):
    global count
    if count > n:
        return prime[n]
    else:
        v = prime [count] + 2
        while count < n:
            if isPrime(v):
                prime.append(v)
                count += 1
            v += 2
        return prime[n]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    print(getPrime (n))
