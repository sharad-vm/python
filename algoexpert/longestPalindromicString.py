"""
https://www.algoexpert.io/questions/Longest%20Palindromic%20Substring
"""
def longestPalindromicSubstring(string):
    # Write your code here.
	longestPalindrome = [0, 1]
	for i in range(1, len(string)):
		odd = getLongestPalindrome(string, i-1, i+1)
		even = getLongestPalindrome(string, i-1, i)
		currentlongest = max(odd, even, key = lambda x: x[1] - x[0])
		longestPalindrome = max(longestPalindrome, currentlongest, key = lambda x: x[1] - x[0])
	return string[longestPalindrome[0]:longestPalindrome[1]]

def getLongestPalindrome(string, leftIdx, rightIdx):
	while leftIdx >= 0 and rightIdx < len(string):
		if string[leftIdx] != string[rightIdx]:
			break
		leftIdx -= 1
		rightIdx += 1
	return [leftIdx + 1, rightIdx]
