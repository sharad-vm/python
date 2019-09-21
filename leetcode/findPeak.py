# Find peak element in a sorted array
# array = [2,3,5,12, 43, 21, 25,29]

# https://www.youtube.com/watch?v=CFgUQUL7j_c
print "Practice makes Perfect!"   

def findPeak (array):
  left, right = 0, len(array)-1
  while left < right:
    mid = (left + right)//2
    if array[mid] > array[mid+1]:
      right = mid
    else:
      left = mid + 1
  return array[left]

#array = [1, 3, 2, 2, 1, -1]
array = [2,3,5,12, 43, 12, 8, 1]
print (findPeak(array))
