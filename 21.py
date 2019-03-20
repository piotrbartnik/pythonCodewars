# tribonacci sequence
def tribonacci(signature, n): 
  if n == 0:
    return []
  if n == 1:
    return [signature[0]]
  g = n
  i = 0
  while n > 0:
    while len(signature) < g:
      signature.append(sum(signature[slice(i,i+3)]))
      i += 1
    n -= 1
  print(signature)

tribonacci([1,1,1], 10)