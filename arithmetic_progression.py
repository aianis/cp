"""1502. Can Make Arithmetic Progression From Sequence
Easy
1K
65
company
Amazon
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

 

Example 1:

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements."""

#Explnarion
#The difference between any two consecutive elements is the same.
# the forumula for an arithmetic progression is: a_n = a_1 + (n-1)d 

#simple and optimal solution
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != d:
                return False
        return True
