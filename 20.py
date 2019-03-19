# find lone element from array
def stray(arr):
  for i in arr:
   if arr.count(i) == 1:
     return i

stray([2, 3, 2, 2, 2])