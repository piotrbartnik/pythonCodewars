# returns position of capital letter
def capitals(word):
  i = 0 
  result = []
  while i < len(word):
    if word[i].isupper():
      result.append(i)
    i += 1
  return result

capitals('CodEWaRs')