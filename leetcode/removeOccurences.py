# Remove all occurrences of given character from array and return modified array with length.
# arr = {'a', 'a', 'a', 'b', 'a'} input = a
# output = {'b'}

print "Practice makes Perfect!"   

def removeOccurences(array, charToRemove):
  length = -1
  for i in range(len(array)):
    if array[i] != charToRemove:
      length += 1
      array[length] = array[i]
  return array[0:length+1]


array = ['a', 'a', 'a', 'b', 'a']
char1 = 'a'
newOccurences = removeOccurences(array, char1)

print (newOccurences)
