def xor(a, b):
	if a == b:
		return 0
	return 1

a, b = map(int, input().split())
print(xor(a, b))