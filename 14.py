def min_max(lst):
  res = []
  lst.sort()
  res.append(lst[0])
  res.append(lst[len(lst)-1])
  return res

min_max([1,2,3,5,4])