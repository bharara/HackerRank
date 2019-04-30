t = int(input())

for j in range(t):
	n = int(input())

	k = 2**n
	s = 0
	for i in list(str(k)):
		s += int(i)
	print(s)	