"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        t = 0
        while 0 in nums:
            for i, num in enumerate(nums):
                if nums[i] == 0:
                    del nums[i]
                    t += 1      
        for j in range(t):
            nums.append(0)  
