def not_string(str):
  if(len(str) < 3 or (str[0] != 'n' or str[1] != 'o' or str[2] != 't')):
    return 'not ' + str
  return str
