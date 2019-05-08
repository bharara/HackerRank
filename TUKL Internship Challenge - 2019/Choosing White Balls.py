cache = {}
def ballGame(depth, bls):
    if bls in cache: return cache[bls]
    if depth == k: return w - bls.count('W')

    res = 0
    l = n - depth
    for i in range(l // 2):
        left = ballGame(depth + 1, bls[:i] + bls[i + 1:])
        right = ballGame(depth + 1, bls[:l - 1 - i] + bls[l - i:])

        res += max(left, right)
    
    res *= 2

    if l % 2:
        res += ballGame(depth + 1, bls[:l//2] + bls[l//2+1:])
    
    cache[bls] = res
    return res

n, k = input().split()
n = int(n)
k = int(k)

balls = input()

w = balls.count('W')

if n == k:
    print(w)
else:
    ans = ballGame (0, balls)
    for i in range(k):
        ans /= n - i
    print(str.format('{0:.7f}', ans))
