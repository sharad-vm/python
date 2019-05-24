"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

"""
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        l = len(A) - 1
        
        while l > 0:
            
            if abs(A[0]) > abs(A[l]):
                A.insert(l, A.pop(0))
                
            A[l] *= A[l]
            
            l -= 1
                
        A[0] *= A[0]
        
        return A
