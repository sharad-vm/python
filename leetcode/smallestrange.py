"""
Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.
"""

class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A) == 1:
            return 0
    
        min_val = min(A)
        max_val = max(A)
        
        if K == 0:
            return max_val - min_val
        
		#To make max_val as close to min_val as possible
        max_val -= K
        
		#if the difference between max_val and min_val is between 0 and K, then result will always be 0
        if max_val - min_val < K:
            return 0
		
		#otherwise the min difference is max_val - min_val + K	
        return max_val - (min_val + K)
