def power(a, b):
	r = 1
	for i in range(b):
		r *= a
	return r
a, b = map(int, input().split())
print(power(a, b))