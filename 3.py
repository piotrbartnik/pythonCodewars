#counting positives and sum negatives

def count_positives_sum_negatives(arr):
  if len(arr) > 0:
    result = [0, 0]
    i = 0
    while i < len(arr):
      if arr[i] > 0:
        result[0] += 1
        i += 1
      elif arr[i] < 0:
        result[1] += arr[i]
        i += 1
      elif arr[i] == 0:
        i += 1    
    return result
  else:
    result = []
    return result

count_positives_sum_negatives([1,2,3,4,-19,-2])