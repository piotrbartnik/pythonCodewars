def descending_order(num):
  res = list(str(num))
  res.reverse()
  return int(''.join(res))

descending_order(123456789)