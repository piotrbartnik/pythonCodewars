# converting binary array to number
def binary_array_to_number(arr):
  res = []
  for i in arr:
    res.append(str(i)) 
  return int("".join(res),2)

binary_array_to_number([1,1,1,1])