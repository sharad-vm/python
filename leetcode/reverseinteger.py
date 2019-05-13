"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
"""

class Solution:
    def reverse(self, x: int) -> int:
              
        x = str(x)
        
        if x[0] == '-':
            
            reverse =  - int(x[len(x):0:-1])
            
        else:
            
            reverse = int(x[::-1])
        
        if reverse < -pow(2, 31) or reverse >= pow(2, 31):
            
            return 0
            
        return reverse
    
    