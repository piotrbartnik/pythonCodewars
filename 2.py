#very simple name abbreviator
def abbrevName(name):
  name = name.split(' ')
  print(name[0][0].capitalize() + '.' + name[1][0].capitalize())

abbrevName("David mendieta")