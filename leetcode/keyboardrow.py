"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
 
Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
"""

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set(['q','w','e','r','t','y','u','i','o','p'])
        row2 = set(['a','s','d','f','g','h','j','k','l'])
        row3 = set(['z','x','c','v','b','n','m'])
        
        result = []
        
        for word in words:
            if set(word.lower()).issubset(row1) or set(word.lower()).issubset(row2) or set(word.lower()).issubset(row3):
                result.append(word)
        return result
                
