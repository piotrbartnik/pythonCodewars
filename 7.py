# count the digit in all squared
def nb_dig(n, d):
  i = 0
  res = []
  while i<=n:
    res.append(pow(i,2))
    i += 1    
  resString = "".join(str(e) for e in res)
  j = 0 
  counter = 0
  while j<len(resString):    
    if int(resString[j]) == d:
      counter += 1
    j += 1
  return counter


nb_dig(5750, 0)