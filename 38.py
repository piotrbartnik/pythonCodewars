def min_sum(arr):
  res = []
  arr.sort()
  while len(arr) > 0:
    res.append(arr.pop(0) * arr.pop(len(arr)-1))
  return sum(res)

min_sum([12,6,10,26,3,24])