def c2i(name):
    s = 0
    for ch in name:
        s += ord(ch)-64
    return s

n = int(input())
lst = []
for k in range(n):
    lst.append(input())

lst.sort()

n = int(input())
for k in range(n):
    name = input()
    print(c2i(name) * (lst.index(name) + 1))