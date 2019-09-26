 
#Suppose you have a long flowerbed in which some of the plots are planted and some are not. 
#However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

#Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, 
#return if n new flowers can be planted #in it without violating the no-adjacent-flowers rule.

#Example 1:
#Input: flowerbed = [1,0,0,0,1], n = 1
  
#Output: True
#Example 2:
#Input: flowerbed = [1,0,0,0,1], n = 2
#Output: False

#bed = [0], n = 1



def newFlowers(bed, n):
  
  for i in range(len(bed)):
    if bed[i] == 0 and (i == len(bed)-1 or bed[i+1] == 0) and (i == 0 or bed[i-1] == 0):
        n -= 1
        bed[i] = 1
    if (n == 0):
        return True
  return False


bed = [0, 0, 0, 1]
n = 3 
print (newFlowers(bed, n))
