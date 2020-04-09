def string_splosion(str):
  s = ''
  t = ''
  for i in range(len(str)):
    t += str[i]
    s += t
  return s
