# uses python 2
# assume numbers list to always have atleast 3 elements
def prod_3(numbers):
	
	# store highest product of 3
	# store highest product of 2
	# store lowest product of 2
	# store highest number
	# store lowest number
  
	highest_prod_3 = 1
	highest_prod_2 = 1
	lowest_prod_2 = 1
	highest = 1
	lowest = 1

	for n in numbers:

		highest_prod_3 = max(highest_prod_2 * n, lowest_prod_2 * n, highest_prod_3)

		highest_prod_2 = max(highest_prod_2, highest * n, lowest * n)
		
		lowest_prod_2 = min(lowest_prod_2, highest * n, lowest * n)

		highest = max(highest, n)

		lowest = min(lowest, n)

	return highest_prod_3
  
# Test cases
# Remember: debugging is half the battle!
numbers = [-100,-5, 1, 30, -10]
print prod_3(numbers)
