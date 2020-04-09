import math
cnt = 1
n = int(input())
while(cnt < n):
	cnt *= 2
if(cnt == n):
	print("YES")
else:
	print("NO")