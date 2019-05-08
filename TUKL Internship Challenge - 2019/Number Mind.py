from random import randint

def shuffle ():
    return str(randint (0, 9))

def misMatch (s):
    miss = 0
    for i in range(k):
        hit = 0
        for j in range(n):
            if s[j] == array[i][j]:
                hit += 1
    
        if (hit > hits[i]):
            miss += hit - hits[i];
        else:
            miss += hits[i] - hit;
    return miss


array = []
hits = []
k = int(input().strip())

for k_c in range(k):
    val, h = input().strip().split()
    array.append(list(val))
    hits.append(int(h))

n = len(array[0])

currentS = ''
for i in range(n):
    currentS += shuffle()

wait = 0
error = misMatch (currentS)
lastError = error

while (error != 0):
    for i in range(n):
        previousDigit = currentS[i]
        currentS = currentS[:i] + shuffle() + currentS[i+1:]

        newError = misMatch(currentS)

        if (newError <= error):
            error = newError
        else:
            currentS = currentS[:i] + previousDigit + currentS[i+1:]


    if error == lastError:
        wait += 1

        if wait == 20:
            r = randint(0,n-1)
            currentS = currentS[:r] + shuffle() + currentS[r+1:]
            error = misMatch(currentS)
            wait = 0
    else:
        wait = 0
        lastError = error

print(currentS)