def string_match(a, b):
  cnt = 0
  for i in range(min(len(a), len(b)) - 1):
    x = a[i:i+2]
    y = b[i:i+2]
    if x == y:
      cnt += 1
  return cnt
