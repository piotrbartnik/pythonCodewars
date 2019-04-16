# unique from array
def find_uniq(arr):
  n = list(set(arr))
  for i in n:
    if arr.count(i) == 1:
      return i


find_uniq([ 1, 1, 1, 2, 1, 1 ])