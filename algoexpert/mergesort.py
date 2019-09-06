
def mergeSort(array):
    # Write your code here.
	if len(array) < 2:
		return array
	mid = len(array)//2
	left = array[:mid]
	right = array[mid:]
	return mergeSortArray(mergeSort(left), mergeSort(right))

def mergeSortArray (lefthalf, righthalf):
	sortedarray = [None] * (len(lefthalf) + len(righthalf))
	k = i = j = 0
	while i < len(lefthalf) and j < len(righthalf):
		if lefthalf[i] < righthalf[j]:
			sortedarray[k] = lefthalf[i]
			i += 1
		else:
			sortedarray[k] = righthalf[j]
			j += 1
		k += 1
	while i < len(lefthalf):
		sortedarray[k] = lefthalf[i]
		i += 1
		k += 1
	while j < len(righthalf):
		sortedarray[k] = righthalf[j]
		j += 1
		k += 1
	return sortedarray
	
	
