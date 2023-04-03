"""Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7]."""

#Approach 
"""1. a) Iterate over the low and high values and print the values 
b) Iteerate over and use modulo to find the odd numbers 
"""

#Example, 
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0 
        for i in range(low, high+1):  #+1 cause it is inclusive 
            if i %2 != 0:   #uses module to check if it is odd by checking if it is even or not. If not even then it is odd!
                count+=1    #counts the numbers of odds in range of low to high+1 
        return count        #return the result
    
#Result: faild cuase the time complexity = O(high-low) which is horrible. 

#Second approach:
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = (high - low) // 2
        if low % 2 != 0 or high % 2 != 0:
            count += 1
        return count
        


