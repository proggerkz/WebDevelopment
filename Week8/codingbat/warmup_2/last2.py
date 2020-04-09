def last2(str):
  cnt = 0 
  if len(str) <= 1:
    return 0
  s = str[-2] + str[-1]
  for i in range(len(str) - 2):
    p = (str[i:i+2])
    if s == p:
      cnt += 1
  return (cnt)