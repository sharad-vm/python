# uses python 2
# merge 2 sorted lists in order
# handles unequal number of elements and empty lists

''' 
Trivia! Python's native sorting algorithm is called Timsort. It's actually optimized for sorting lists where subsections of the lists are already sorted. For this reason, a more naive algorithm:

  def merge_sorted_lists(arr1, arr2):
    return sorted(arr1 + arr2)

is actually faster until nn gets pretty big. Like 1,000,000.
'''

def merge_lists(list1, list2):
	#initialize a merged_list list
	merged_list = [None] * (len(list1) + len(list2))

	start_index_1 = 0
	start_index_2 = 0
	merged_index = 0

	while merged_index < len(merged_list):
		
		list1_exhausted = start_index_1 >= len(list1)
		list2_exhausted = start_index_2 >= len(list2)

		# if list1 is not exhausted and list2 is either exhausted
		# or list1 element is greater than list2 element 
		# then add list1 element to merged_list
		if (not list1_exhausted) and (list2_exhausted or 
									 (list1[start_index_1] < list2[start_index_2])):
			merged_list[merged_index] = list1[start_index_1]
			start_index_1 += 1

		# if list2 is not exhausted and list1 is either exhausted
		# or list2 element is greater than list1 element 
		# then add list2 element to merged_list
		elif (not list2_exhausted) and (list1_exhausted or 
									   (list1[start_index_1] >= list2[start_index_2])):
			merged_list[merged_index] = list2[start_index_2]
			start_index_2 += 1

		merged_index += 1

	return merged_list

# Test
list1 = [3, 4, 6, 10, 11]
list2 = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print merge_lists(list1, list2)
