# counting growth of populations
def nb_year(p0, percent, aug, p):
  counter = 0
  while p0 < p:
    p0 += p0*(percent/100)
    p0 += aug
    counter += 1
  return counter

nb_year(1500, 5, 100, 5000)