# Palindrome
def palin(num):
    return str(num) == str(num)[::-1]


# Create a list of are Palindromes in Range
p = []
for a in range(100, 1000):
    for b in range(a, 1000):
        if palin(a*b):
           p.append (a*b)
p = sorted (p)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
            
    val = 0
    for i in p:
        if i < n:
            val = i
        else:
            break

    print(val)
