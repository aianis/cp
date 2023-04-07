"""Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15"""

#Approach: 
# 1. We can use the modulo operator to get the last digit of the number.
# 2. We can use the floor division operator to remove the last digit of the number.
# 3. We can use the product and sum variables to store the product and sum of the digits.
# 4. We can use a while loop to iterate until the number becomes 0.
# 5. We can use the product and sum variables to store the product and sum of the digits.

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        while n:
            product *= n % 10
            sum += n % 10
            n = n // 10
        return product - sum
    


#Time complexity: O(log n)  #as the input size grows, the number of operations also increases
#Space complexity: O(1)  #constant space is used as the number of variables remain constant


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0 
        result = 0 
        for num in str(n):
            product *= int(num)
            sum += int(num)
        result = product - sum 
        return result 

        #Solution: easy to understand, but lil slower than than the previous one with O(n)

