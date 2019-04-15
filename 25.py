def toJadenCase(string):
  string = string.split(' ')
  iterator = 0
  result = []
  while iterator < len(string):
    result.append(string[iterator][0].upper()+(string[iterator][1:]))
    iterator += 1
  return " ".join(result)

toJadenCase("How can mirrors be real if our eyes aren't real")