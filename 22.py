# count elements occurence in array
from collections import Counter
def count(array):
    return dict((x,array.count(x)) for x in set(array))