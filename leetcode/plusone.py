"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = 1
        carry = 0
        if len(digits) == 1 and digits[0] == 9:
            return [1, 0]
        result = []
        for d in digits[::-1]:
            if d != 9:
                d += add
                add = 0
                carry = 0
            elif add == 1:
                d = 0
                carry = 1
            result.append(d)
        if carry == 1:
            result.append(1)
        return result[::-1]
        
