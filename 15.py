# closest division of 5

def round_to_next5(n):
  if (n == 0) or (abs(n)%5 == 0):
    return n
  elif(n%5 != 0):
    i = 1
    while (n%5 != 0):
      n = n + i
  return n 

round_to_next5(-16)