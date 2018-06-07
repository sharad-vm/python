# uses python 2	
# count sort method
def count_sort(scores, highest_score):
	# initialize a list with 0's and
	# length as much as the highest score 
	sorted_list = [0] * (highest_score + 1)
	sorted_scores = []
	# for every number in the score, 
	# add 1 to that index position in sorted_list
	for num in scores:
		sorted_list[num] += 1

	# for all elements in the sorted_list
	# greater than 0, repeat the index 
	# as many times as the value
	for n in range(len(sorted_list)):
		if sorted_list[n] > 0:
			for times in range(sorted_list[n]):
				sorted_scores.append(n)

	return sorted_scores
  
# Test cases
# Remember: debugging is half the battle!
highest_score = 10
scores = [4, 4, 10, 3, 8]
print count_sort(scores, highest_score)
