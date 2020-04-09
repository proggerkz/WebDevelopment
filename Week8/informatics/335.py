a = int(input())
b = int(input())
import math
for i in range(a, b + 1):
	x = int(math.sqrt(i))
	if(x * x == i):
		print(i, end = ' ')