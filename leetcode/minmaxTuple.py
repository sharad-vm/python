#Given an array, return a tuple of (minElem, maxElem)

# arr = {2, 4, 9, 23, 89}, min = float.inf, max = float.neg_inf
# output = (2, 89)

def minmaxTuple(array):
  maximum = minimum = array[0]
  
  for n in array[1:]:
    minimum = min(minimum, n)
    maximum = max(maximum, n)
  
  return (minimum, maximum)

array = [122, -90909090904, 9, 23, 89]

print (minmaxTuple(array))
