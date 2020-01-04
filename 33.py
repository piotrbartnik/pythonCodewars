def add_letters(*letters):
  sum = 0
  for i in letters:
    sum += ord(i) - ord('a') + 1
  
  if sum >= ord('z') - ord('a'):
    sum = sum%(ord('z') - ord('a'))
  
  return chr(ord('a') - 1 +sum)

add_letters('c')