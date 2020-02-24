"""
Write a function that takes an unsigned integer and return the number of '1'
 bits it has (also known as the Hamming weight).

Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a
total of three '1' bits.
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += 1
            n &= (n-1)
        return ans # bin(n).count('1')