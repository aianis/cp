"""

    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a ***linear runtime complexity*** and use only ***constant extra space***.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.


"""

#simple solution using hashsets 

class Solution:
    def singleNumber(nums):
        #hashset for storing seen nums 

        seen = set()

        #traverse the array to check for duplicate and remove them 
        for num_seen in nums:
            if num_seen in seen:
                seen.remove(num_seen)
            else:
                seen.add(num_seen)

        if seen:
            return seen.pop()