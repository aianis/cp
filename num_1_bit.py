"""Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
 

Example 1:

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits."""

#Approach: Bitwise operations 

#Explanation: 
# 1. We can use the bitwise AND operator to check if the last bit is 1 or not.
# 2. If the last bit is 1, we increment the count.
# 3. We then right shift the number by 1 bit.
# 4. We repeat the above steps until the number becomes 0.


class Solution: 
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if n & 1:
                count += 1
            n = n >> 1
        return count
    
#Time complexity: O(log n)  #as the input size grows, the number of operations also increases
#Space complexity: O(1)  #constant space is used as the number of variables remain constant


#Faster solution
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n = n & (n - 1)
        return count
    


