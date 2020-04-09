def front_times(str, n):
  s = ''
  for i in range(min(len(str), 3)):
    s += str[i]
  t = ''
  for i in range(n):
    t += s
  return t