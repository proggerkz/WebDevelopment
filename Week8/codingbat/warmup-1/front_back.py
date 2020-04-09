def front_back(str):
  if(len(str) <= 1):
    return str
  stp = ''
  for i in range(1, len(str) - 1):
    stp += str[i]
  return '{}{}{}'.format(str[-1], stp, str[0])
