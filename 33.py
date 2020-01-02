def add_letters(*letters):
  sum = 0
  for i in letters:
    sum += ord(i) - ord('a')
  
  if sum >= ord('z') - ord('a'):
    return chr(sum%(ord('z') - ord('a'))+ord('a'))

  return chr(sum+ord('a'))

  # print(ord(letters)-ord('a'))

add_letters('z', 'a')