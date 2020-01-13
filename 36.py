def descending_order(num):
  res = list(str(num))
  res.sort()
  res.reverse()  
  return int(''.join(res))

descending_order(124356789)