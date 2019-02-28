#invert values

def invert(lst):
  i = 0
  while i<len(lst):
    if lst[i] < 0:
      lst[i] = abs(lst[i])
      i += 1
    else:
      lst[i] = -lst[i]
      i += 1
  return lst

invert([1,-2,3,-4,5])