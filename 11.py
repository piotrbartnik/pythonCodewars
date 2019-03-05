import math  
def is_square(n):
  return   math.sqrt(n).is_integer() if n >=0 else False
  
is_square(-1)
