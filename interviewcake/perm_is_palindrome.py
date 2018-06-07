# uses python 2
# assume string to always be lower case
def perm_is_palindrome(string):
	
	char_pair = set()

	# if there is only 1 character
	# that occurs odd number of times,
	# returns T else F
	for char in string:
		if char in char_pair:
			char_pair.remove(char)

		else:
			char_pair.add(char)

	return len(char_pair) <= 1 
  
# Test cases
# Remember: debugging is half the battle!
string = "aneyna"
print perm_is_palindrome(string)
