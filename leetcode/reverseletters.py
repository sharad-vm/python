"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
"""

class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        i = 0
        j = len(S)-1
        
        reverse = []
        
        for c in S:
            if c.isalpha():
                while not S[j].isalpha():
                    j -= 1
                reverse.append(S[j])
                j -= 1
            else:
                reverse.append(S[i])
                
            i += 1
            
        return ''.join(reverse)
