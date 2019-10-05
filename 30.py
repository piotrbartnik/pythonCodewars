def sort_array(ar):
  odd_list = []
  for i in ar:
    if i%2 != 0:
      odd_list.append(i)
  odd_list.sort()
  i = 0
  while i < len(ar):
    if ar[i]%2 != 0:
      ar[i] = odd_list[0]
      odd_list.pop(0)
    i += 1
  return ar
