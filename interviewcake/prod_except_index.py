# uses python 2
# product of all except the current element
# using division
def prod_except_index(numbers):

	prod = 1
	
	for n in numbers:
		prod = prod * n
	return  [prod/n for n in numbers]

# Test cases
# Remember: debugging is half the battle!
numbers = [1, 7, 3, 4]
print prod_except_index(numbers)

# without using division
def prod_except_at_index(numbers):

	# initialize a list 
	product_except_at_index = [None] * len(numbers)
	# iterate and store a variable
	product_so_far = 1

	for n in range(len(numbers)):
		product_except_at_index[n] = product_so_far
		product_so_far *= numbers[n]

	product_so_far = 1

	for n in range(len(numbers)-1, -1, -1):
		product_except_at_index[n] *= product_so_far
		product_so_far *= numbers[n]

	return product_except_at_index
  
# Test cases
# Remember: debugging is half the battle!
numbers = [1, 2, 6, 5, 9]
print prod_except_at_index(numbers)
