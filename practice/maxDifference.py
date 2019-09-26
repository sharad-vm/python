# Given m arrays, and each array is sorted in ascending order. 
# Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. 
# We define the distance between two integers a and b to be their absolute difference |a-b|. 
# Your task is to find the maximum distance.

#Input: 
#[
#[2,3],
#[1,4,5],
#[2,3]]
#Output: 4
#Explanation: 
#One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

def maxDistance(nums):
  minimum = nums[0][0]
  maximum = nums[0][-1]
  maxdiff = 0
  for i in range(1, len(nums)):
    maxdiff = max(maxdiff, abs(nums[i][-1] - minimum), abs(maximum - nums[i][0]))
    maximum = max(maximum, nums[i][-1])
    minimum = min(minimum, nums[i][0])
  return maxdiff
    
nums = [
[1,2,3],
[0,4,5],
[2,3]]
print (maxDistance(nums))
