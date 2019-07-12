"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s=='' and t=='':
            return True
        if len(s) != len(t):
            return False
        s_set = set(s)
        
        for c in s_set:
            s_count = s.count(c)
            t_count = t.count(c)
            if s_count != t_count:
                return False
        return True
