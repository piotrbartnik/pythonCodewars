def who_is_paying(name):
  res = []
  if len(name) > 2:
    res.append(name)
    res.append(name[0:2])
  else:
    res.append(name)
  return res

who_is_paying("I")