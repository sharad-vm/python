# Find second maximum value in an array
array = [2,5,1,7,3,9,11,16,9,8]
#output = 11

def findSecondMax(array):
  firstmax = secondmax = array[0]
  for i in range(1,len(array)):
    if array[i] > firstmax:
      secondmax = firstmax
      firstmax = array[i]
  return secondmax

print(findSecondMax(array))
