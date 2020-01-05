def find_all(array, n):
  result = []
  i = 0
  while i < len(array):
    if array[i] == n:
      result.append(i)
    i += 1
  return result

find_all([6, 9, 3, 4, 3, 82, 11], 3)