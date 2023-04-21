"""976. Largest Perimeter Triangle

Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

Example 1:

Input: nums = [2,1,2]
Output: 5
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
Example 2:

Input: nums = [1,2,1,10]
Output: 0
Explanation: 
You cannot use the side lengths 1, 1, and 2 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.
 

Constraints:

3 <= nums.length <= 104
1 <= nums[i] <= 106"""


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int: #
        nums.sort(reverse=True)  # sort the list in descending order
        for i in range(len(nums)-2):  # loop through the list excluding las two elements cause we need 3 elements to form a triangle
            if nums[i] < nums[i+1] + nums[i+2]:   # if the first element is less than the sum of the next two elements
                return nums[i] + nums[i+1] + nums[i+2]  # return the sum of the three elements
        return 0 # if the above condition is not met return 0
    
    