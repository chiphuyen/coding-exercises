'''
This problem is from leetcode.com
https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output:  321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only hold integers
within the 32-bit signed integer range. For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.
'''


class Solution(object):
    def helper(self, x):
        if x < 10:
            return str(x)
        return str(x % 10) + self.helper(x // 10)

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = int(self.helper(abs(x)))
        return (r < 2 ** 31) * ((x > 0) - (x < 0)) * r


solver = Solution()
assert solver.reverse(-123) == -321
assert solver.reverse(120) == 21
assert solver.reverse(10) == 1
assert solver.reverse(-1) == -1
