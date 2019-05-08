def abbreviation(a,b):

    isTrue = [[False for x in range(len(b)+1)] for y in range(len(a)+1)]
    isTrue[0][0]=True

    for i in range(len(a)):        
        for j in range(len(b) + 1):
            if (isTrue[i][j]):
                if j < len(b):
                    isTrue[i+1][j+1] = a[i].upper() == b[j]
                if a[i].islower():
                    isTrue[i+1][j] = True

    if isTrue[len(a)][len(b)]:
        return "YES"
    return "NO"

q = int(input())

for q_itr in range(q):
    a = input()
    b = input()
    print(abbreviation(a, b))
