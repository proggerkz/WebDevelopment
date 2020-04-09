def front3(str):
  stp = ''
  x = min(3, len(str))
  for i in range(x):
    stp += str[i]
  return stp + stp + stp
