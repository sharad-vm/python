# uses python 2
# this algorithm is known as Fisher-Yates or Knuth shuffle
import random

def get_random(floor, ceiling):
	return random.randrange(floor, ceiling+1)

def shuffle(list):
	if len(list)<2:
		return list

	list_length = len(list)

	for index in range(len(list)-1):

		shuffled_index = get_random(index, len(list)-1)

		if shuffled_index != index:
			list[index], list[shuffled_index] = \
			list[shuffled_index], list[index]

	return list

# Test cases

numbers = [1, 2, 6, 5, 9, 11, 78]
print shuffle(numbers)
