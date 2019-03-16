# sorted list of unique letters form two arrays

def longest(s1, s2):
  return "".join(sorted(list(set(s1+s2))))  

longest("loopingisfunbutdangerous", "lessdangerousthancoding")