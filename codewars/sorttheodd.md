##### You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

##### Example
> sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

---

```python
def sort_array(source_array):
    # Return a sorted array.
    odd=[]
    sorted_array=[]
    for n in source_array:
        if n%2!=0:
           odd.append(n)
    odd=sorted(odd)
    for n in source_array:
        if n%2==0:
           sorted_array.append(n)
        else:
           sorted_array.append(odd.pop(0))
    return sorted_array
```
```python 
#clever solution
def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]
```
