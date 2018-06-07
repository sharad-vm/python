# uses python 2
# assume string to always be lower case
def prod_4(numbers):
	
	# store highest product of 4
	# store highest product of 3
	# store lowest product of 3
	# store highest product of 2
	# store lowest product of 2
	# store highest number
	# store lowest number
	highest_prod_4 = 1
	highest_prod_3 = 1
	lowest_prod_3 = 1
	highest_prod_2 = 1
	lowest_prod_2 = 1
	highest = 1
	lowest = 1

	for n in numbers:

		highest_prod_4 = max(highest_prod_3 * n, lowest_prod_3 * n, highest_prod_4)

		highest_prod_3 = max(highest_prod_2 * n, lowest_prod_2 * n, highest_prod_3)

		lowest_prod_3 = min(lowest_prod_2 * n, lowest_prod_2 * n, lowest_prod_3)

		highest_prod_2 = max(highest_prod_2, highest * n, lowest * n)
		
		lowest_prod_2 = min(lowest_prod_2, highest * n, lowest * n)

		highest = max(highest, n)

		lowest = min(lowest, n)

	return highest_prod_3
  
# Test cases
# Remember: debugging is half the battle!
numbers = [-100,-5, 1, 3, -10, 7, 8]
print prod_4(numbers)

