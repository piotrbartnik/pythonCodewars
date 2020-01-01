def factorial(n):
  if n == 0:
    return 1
  x = list(range(1, n+1))
  sum = 1

  for i in x:
    sum *= i
  return sum


factorial(7)
