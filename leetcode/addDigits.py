"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        sum = 0
        
        while num > 0:
            n,num = num%10,num//10   
            sum += n          
        if sum>9:
            return self.addDigits(sum)
        return sum
"""
Follow up:
Could you do it without any loop/recursion in O(1) runtime?

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if (num%9 != 0) or (num == 0):
            return num % 9
        else:
            return 9
"""
