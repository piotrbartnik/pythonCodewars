#reverse array with susequent nums
def reverse_seq(n):
  arr = []
  for x in range(n):
    arr.append(x+1) 
  return list(reversed(arr))

reverse_seq(5)