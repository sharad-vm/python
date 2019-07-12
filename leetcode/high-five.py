"""
Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.

 

Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.
"""
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        avgScores = {}
        
        for s in items:
            if s[0] in avgScores:
                avgScores[s[0]].append(s[1])
            else:
                avgScores[s[0]] = [s[1]]
        
        result = []
        for i in avgScores:
            temp = avgScores[i]
            temp.sort(reverse = True)
            temp = temp[0:5]
            avg = sum(temp)//5

            result.append([i,avg])

        return result
