import re
def prefill(n,v=0):
  if isinstance(n, float):
    if n < 1 and n !=0:
      return 'err'
  if v is None or n is None :
    return 'failed with number 0'  
  if not isinstance(n, int):
    if bool(re.search('[a-z]', n)):
      return 'err' 
  n = int(float(n))  
  result = [v] * n  
  return result