"""
https://www.algoexpert.io/questions/Find%20Three%20Largest%20Numbers
"""
def findThreeLargestNumbers(array):
    # Write your code here.
	threeLargest = [None, None, None]
	
	for num in array:
		if threeLargest[2] is None or num > threeLargest[2]:
			shiftandUpdate(threeLargest, num, 2)
		elif threeLargest[1] is None or num > threeLargest[1]:
			shiftandUpdate(threeLargest, num, 1)		
		elif threeLargest[0] is None or num > threeLargest[0]:
			shiftandUpdate(threeLargest, num, 0)	
	return threeLargest

def shiftandUpdate(array, num, idx):
	for i in range(idx+1):
		if i == idx:
			array[i] = num
		else:
			array[i] = array[i+1]
