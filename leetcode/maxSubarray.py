#Find maximum subarray in given array
#input = [-2, -1, -3, 24,5, -6]
#output = 13 and [3, 4, 5]

print "Practice makes Perfect!"   

def maxSubarray(array):
  maxSofar = array[0]
  maxEndinghere = array[0]
  start = end = 0
  for i in range(1,len(array)):
    num = array[i]
    if num > maxEndinghere + num:
      maxEndinghere = num
      start = i
    else:
      maxEndinghere += num
      end = i
    maxSofar = max(maxSofar, maxEndinghere)
    
  return maxSofar, array[start:end]

array = [-2, -1, -3, 24,5, -6]
print (maxSubarray(array))
