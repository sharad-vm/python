# Merge two sorted arrays
# arr1 = {10, 30, 34}
# arr2 = {5, 15, 24, 40, 45}

print "Practice makes Perfect!"   

def mergeArrays(arr1, arr2):
  arr3 = []
  i = j = 0
  while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
      arr3.append(arr1[i])
      i += 1
    else:
      arr3.append(arr2[j])
      j += 1
      
  if i < len(arr1):
    arr3.extend(arr1[i:])

  if j < len(arr2):
    arr3.extend(arr2[j:])
    
  return arr3

arr1 = [10, 30, 34]
arr2 = [5, 15, 24, 40, 45]
        
print (mergeArrays(arr2, arr1))
  

