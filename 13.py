def double_char(s):
  string = ''
  result = []
  for i in s:
    result.append(i + i)
  return string.join(result)
  
double_char("String")