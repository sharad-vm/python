"""
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.
"""
def peakIndexInMountainArray( A):
    """
    :type A: List[int]
    :rtype: int
    """
    if len(A)<3 or len(A)>10000:
        return "Not a mountain array"
    else:
        start = 0
        end = len(A)-1
        
        while start < end:
            mid = (start + end)//2
            
            if A[mid-1]<A[mid] and A[mid]>A[mid+1]:
                return mid
            elif A[mid-1]<A[mid] and A[mid]<A[mid+1]:
                start = mid
            else:
                end = mid
