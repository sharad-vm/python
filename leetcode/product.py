#Given an array, return array of product of all numbers except itself.
# arr = {{2, 3}, 4 , 5}
# output = {60, 40, 30, 24}

def product (array):
  product = 1
  result = [None] * len(array)
  result[0] = product
  
  for i in range(1,len(array)):
    result[i] = result[i-1] * array[i-1]  #{1, 2, 6, 24}
  
  for i in range(len(array)-2, -1, -1):
    product = product * array[i+1]
    result[i] *= product #
 
  return result
  #return [l*r for l,r in zip(result, right)]  
    
array = [2,3,4,5]
print (product(array))
