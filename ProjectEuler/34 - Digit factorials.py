def factorial (n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def factorial_of_digits (n):

    total = 0
    for i in range(len(str(n))):
        total += factorial (n % 10)
        n //= 10
    return total


n = int(input())

total = 0
for i in range(10, n):
    if factorial_of_digits (i) % i == 0:
        total += i
print(total)
