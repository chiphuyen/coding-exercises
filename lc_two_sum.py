'''
Problem on leetcode.com
https://leetcode.com/problems/two-sum/description/

Given an array of integers, return indices of the two numbers such that
they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Note: I didn't come up with the solution.
This elegant solution was posted as a comment by xiaohua on leetcode
'''


def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    seen = {}
    for idx, value in enumerate(nums):
        compl = target - value

        if compl in seen:
            return [seen[compl], idx]

        seen[value] = idx
    return []


assert two_sum([2, 3, 5, 1], 6) == [2, 3]
assert two_sum([2, 3, 5, 1], 8) == [1, 2]
assert two_sum([2, 3, 5, 1], 10) == []
assert two_sum([2, 3, 3, 1], 6) == [1, 2]
