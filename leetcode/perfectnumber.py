"""
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14

Note: The input number n will not exceed 100,000,000. (1e8)
"""

class Solution:
    def factors(num):
        
        factors = set(1)
        i = 2

        while i < num:
            if num % i == 0:
                factors.add(i)
        
            i += 1
        return factors
    
    def checkPerfectNumber(num):
    """
    :type num: int
    :rtype: bool
    """
        
        if num < 6:
            return false
    
        else:
            return sum(self.factors(num)) == num
