"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        
        for i in nums:
            try:
                nums_dict.pop(i)
            except:
                nums_dict[i] = 1
        
        return nums_dict.popitem()[0]
        
        #solution 2 - one liner using set()
        #return 2* sum(set(nums)) - sum(nums)
        
        """
        solution 3 - using XOR
        
        a = 0
        for i in nums:
          a ^= i
         
        return a
        """
        
    
