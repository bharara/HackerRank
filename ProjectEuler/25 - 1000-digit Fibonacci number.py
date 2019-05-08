
limit = 25000
fib = [0, 1]
for i in range(2, limit):
	fib.append(fib[i-1] + fib[i-2])


fibDig = [0, 1]
for x in fib:
	if len(str(x)) >= len(fibDig):
		fibDig.append(fib.index(x))






n = 50
print(fibDig[n])