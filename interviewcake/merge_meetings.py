# Write a function to reverse a list of strings in place 
def reverse_in_place(arg):

	for c in range(len(list)/2):
		# store the other side of the list
		switch = list[-c-1]
		# assign current character to the other side of the list 
		list[-c-1] = list[c] 
		# assign the other side of the list to the current character
		list[c] = switch

	return list 

# Test cases
# Remember: debugging is half the battle!
list = ['a','b', 'c', 'd', 'e']
print reverse_in_place(list)

# interview cake version
def reverse(l):

	left_index = 0
	right_index = len(l)-1

	while left_index < right_index:
		l[left_index], l[right_index] = l[right_index], l[left_index]

		left_index += 1
		right_index -= 1

	return l

# Test cases
# Remember: debugging is half the battle!
l = ['a','b', 'c', 'd', 'e']
print reverse(l)
