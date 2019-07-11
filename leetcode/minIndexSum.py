"""
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
"""

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict = {}
        maxindexSum = len(list1) + len(list2) - 1
        restaurants = []
        for i1, r1 in enumerate(list1):
            dict[r1] = i1
            
        for i2, r2 in enumerate (list2):
            if r2 in dict:
                if dict[r2] + i2 < maxindexSum:
                    maxindexSum = dict[r2] + i2
                    restaurants.clear()
                    restaurants.append(r2)
                elif dict[r2] + i2 == maxindexSum:
                    restaurants.append(r2)
                    
        return restaurants
