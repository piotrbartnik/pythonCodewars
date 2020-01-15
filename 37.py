def divisors(n):
  result = []
  iterator = 1
  while iterator <= n:
    if n%iterator == 0:
      result.append(iterator)
    iterator += 1
  
  return len(result)


divisors(4)