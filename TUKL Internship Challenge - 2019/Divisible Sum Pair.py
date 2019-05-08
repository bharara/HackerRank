# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    c = 0
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                c += 1
    return c

n, k = input().split()
n = int(n)
k = int(k)

ar = list(map(int, input().rstrip().split()))

print(divisibleSumPairs(n, k, ar))
