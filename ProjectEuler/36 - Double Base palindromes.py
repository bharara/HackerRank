def convB(num,k):
    convStr = "0123456789"
    if num<k:
        return convStr[num]
    else:
        return convB(num//k, k) + convStr[num% k]

def reverse (n):
    return n[::-1]

def palin(n):

    n = str(n)
    l = len(n)

    if l % 2:
        return n[:l//2] == reverse(n[l//2 + 1:])
    return n[:l//2] == reverse(n[l//2:])

n, k = input().split()
n = int(n)
k = int(k)

total = 0
for i in range(1, n):
    if palin(i) and palin (convB(i, k)):
        # print(i)
        total += i

print(total)