def strongest_even(n, m):
  nres = 0
  mres = 0
  while n%2 == 0:
    n = n/2
    nres += 1
  while m%2 ==0:
    m = m/2
    mres += 1

  if nres > mres:
    return nres
  return mres

strongest_even(48, 56)