k = 1000000

## Creating array where prime is 1
isPrime = [1] * k
isPrime [0] = isPrime [1] = 0
for i in range(4, k, 2):
    isPrime [i] = 0

for i in range(3, int(k**0.5)+1, 2):
    if isPrime[i]:
        for j in range (i*i, k, i):
            isPrime [j] = 0

## Creating Running Sum array
sumP = [0] * k
rs = 0
for i in range(k):
    if isPrime[i]:
        rs += i
    sumP [i] = rs


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    print(sumP[n])