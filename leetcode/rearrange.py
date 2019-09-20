#Re-arrange sorted array in max min form
# arr = [2, 4, 7, 18, 90]
# output = {2, 90, 4, 18, 7} {min, max, min, max}

print "Practice makes Perfect!"   

def rearrange(array):
  i, j = 0, len(array)-1
  result = []
  while i <= j:
    if i != j:
      result.append(array[i])
      result.append(array[j])
    else:
      result.append(array[i]) 
    i += 1
    j -= 1
    
  return result

array = [2, 4, 7, 18, 90, 103]
print (rearrange(array))
