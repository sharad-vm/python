"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

1, 2, 3

1 2 3 => 1, 2, 3
1 3 2
2 3 1


public List<List<Integer>> permute(int[] nums) {
   List<List<Integer>> list = new ArrayList<>();
   // Arrays.sort(nums); // not necessary
   backtrack(list, new ArrayList<>(), nums);
   return list;
}

private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums){
   if(tempList.size() == nums.length){
      list.add(new ArrayList<>(tempList));
   } else{
      for(int i = 0; i < nums.length; i++){ 
         if(tempList.contains(nums[i])) continue; // element already exists, skip
         tempList.add(nums[i]);
         backtrack(list, tempList, nums);
         tempList.remove(tempList.size() - 1);
      }
   }
} 

"""
from copy import deepcopy

def permute (nums):
  list = []
  newlist = []
  backtrack(list, newlist, nums)
  return list

def backtrack(list, templist, nums):
  if len(templist) == len(nums):
    addedlist = templist[:]
    list.append(addedlist)
  else:
    for n in nums:
      if n in templist:
        continue
      templist.append(n)
      backtrack(list, templist, nums)
      templist.pop()
      
nums = [1,2,3]
print(permute(nums))
