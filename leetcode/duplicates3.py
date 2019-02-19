"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
"""

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        
        n = {}
        for i, v in enumerate(nums):
            if len(n) > 2*t:
                for index in range(v-t, v+t+1):
                    if index in n and i-n[index] <= k:
                        return True
            else:
                for index in n:
                    if abs(v-index) <= t and i-n[index] <= k:
                        return True
            n[v] = i
        
        return False
            
