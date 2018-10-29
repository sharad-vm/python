"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
"""
class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        prev = float('-inf')
        distance = []

        for i,x in enumerate(S):
            if x == C:
                prev = i
            distance.append(i - prev)
    
        prev = float('inf')
        for i in range(len(S)-1, -1, -1):
            if S[i] == C:
                prev = i
            distance[i] = min(distance[i],prev - i)
    
        return distance
