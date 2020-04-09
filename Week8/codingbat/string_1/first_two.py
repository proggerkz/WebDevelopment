def first_two(str):
  pat = ''
  for i in range(min(2, len(str))):
    pat += str[i]
  return pat

