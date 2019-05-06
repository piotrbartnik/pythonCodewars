# multiplication table
def multiplication_table(row,col):
  first_list = list(range(1, col+1))
  result = []
  result.append(first_list)
  i = 2
  while i < row+1:
    multiply_result = []
    for j in first_list:
      multiply_result.append(j*i)
    result.append(multiply_result)
    i+=1
  return result

multiplication_table(3,4)