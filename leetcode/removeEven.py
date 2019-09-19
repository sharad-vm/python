#Write a program that removes even integers from given array and return new array. Do not use a new array.
# input arr = {2,2,4,5,6}
# output = {3,5} len = 2, endPos = 1
#print "Practice makes Perfect!"   

def removeEven(array):
  
  oddPtr = -1
  for i in range(len(array)):
    if array[i] % 2 == 1:
      oddPtr += 1
      array[oddPtr] = array[i]
  return oddPtr+1
  
array = [-1,-2, 0,2,3,4,5,6,8]

print(removeEven(array))
