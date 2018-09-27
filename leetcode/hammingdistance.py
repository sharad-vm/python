"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""
class Solution(object):
   
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        x = self.convertToBinary(x)
        y = self.convertToBinary(y)
        
        i = len(x)-1
        count = 0
        
        while i >= 0:
            if x[i] != y[i]:
                count += 1
            i-=1
        return count
        
    def convertToBinary(self, num):
        binary = [0] * 32
        i = 32 - 1
        
        while (num > 0):
            binary[i] = num % 2
            num //= 2
            i-= 1
        
        return binary
