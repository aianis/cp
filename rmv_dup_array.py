"""Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such 
that each unique element appears only once. The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order 
they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

"""
############################################################################################################################################################################
#Explnation
############################################################################################################################################################################
"""The first thing to do is to check if the length of the array is 0 or 1. 
If it is, then the number of unique elements is the same as the length of the array. 
If the length is greater than 1, then we need to use two pointers to keep track of the unique elements. 
The first pointer will be used to keep track of the unique elements and the second pointer will be used to iterate through the array. 
We will start the first pointer at index 0 and the second pointer at index 1. 
We will iterate through the array until the second pointer reaches the end of the array. 
At each iteration, we will check if the element at the second pointer is equal to the element at the first pointer. 
If it is, then we will increment the second pointer. 
If it is not, then we will increment the first pointer and set the element at the first pointer to the element at the second pointer.
 We will continue this process until the second pointer reaches the end of the array. 
 At this point, the first pointer will be pointing to the last unique element in the array. 
 We will return the first pointer plus 1 as this will be the number of unique elements in the array.
    
"""

############################################################################################################################################################################
#Approach 1: Two Pointers
############################################################################################################################################################################

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            first_pointer = 0
            second_pointer = 1
            while second_pointer < len(nums):
                if nums[second_pointer] == nums[first_pointer]:
                    second_pointer += 1
                else:
                    first_pointer += 1
                    nums[first_pointer] = nums[second_pointer]
                    second_pointer += 1
            return first_pointer + 1
        

############################################################################################################################################################################
#Approach 2: Pythonic
############################################################################################################################################################################

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            nums[:] = sorted(set(nums))
            return len(nums)

