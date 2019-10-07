'''
This problem is from leetcode
https://leetcode.com/problems/median-of-two-sorted-arrays/description/

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity
should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5

My solution:
    I know it's super ugly. I will update it when I can come up
    with a better solution.
    This solution was accepted by leetcode
'''

import math


class Solution(object):
    def median(self, nums):
        n = len(nums)
        if n == 0:
            return None
        if n % 2 == 0:
            return (nums[n // 2] + nums[n // 2 - 1]) / 2
        else:
            return nums[n // 2]

    def median3(self, num1, num2, num3):
        if num1 <= num2:
            return num2
        if num1 <= num3:
            return num1
        return num3

    def median4(self, num1, num2, num3, num4):
        if num1 <= num2:
            return (num2 + num3) / 2
        if num1 <= num4:
            return (num1 + num3) / 2
        return (num3 + num4) / 2

    def median6(self, a1, a2, b1, b2, b3, b4):
        if a2 <= b1:
            return (b1 + b2) / 2
        if a1 <= b1 and a2 <= b3:
            return (a2 + b2) / 2
        if (a1 <= b2 and a2 > b3):
            return (b2 + b3) / 2
        if a1 < b2 and a2 <= b3:
            return (a2 + b2) / 2
        if a1 > b2 and a2 <= b3:
            return (a1 + a2) / 2
        if a1 <= b4 and a2 > b3:
            return (a1 + b3) / 2
        return (b3 + b4) / 2

    def findMedianHelper(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        if m == 0:
            return self.median(nums2)
        if m == 1:
            if n == 1:
                return (nums1[0] + nums2[0]) / 2
            if n % 2 == 0:
                return self.median3(nums1[0], nums2[n // 2 - 1], nums2[n // 2])
            return self.median4(nums1[0],
                                nums2[n // 2 - 1],
                                nums2[n // 2],
                                nums2[n // 2 + 1])

        if m <= 2:
            if n <= 3:
                return self.median(sorted(nums1 + nums2))
            else:
                if n % 2 == 1:
                    temp = sorted(nums1 + [nums2[n // 2 - 1],
                                           nums2[n // 2],
                                           nums2[n // 2 + 1]])
                    return self.median(temp)
                else:
                    return self.median6(nums1[0],
                                        nums1[1],
                                        nums2[n // 2 - 2],
                                        nums2[n // 2 - 1],
                                        nums2[n // 2],
                                        nums2[n // 2 + 1])

        mid1 = int(math.ceil(m / 2) - 1)
        mid2 = n // 2

        if nums1[mid1] <= nums2[mid2]:
            return self.findMedianHelper(nums1[mid1:], nums2[:-mid1])
        else:
            return self.findMedianHelper(
                nums1[:mid1 + 1], nums2[m - mid1 - 1:])

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) <= len(nums2):
            return self.findMedianHelper(nums1, nums2)
        else:
            return self.findMedianHelper(nums2, nums1)


solver = Solution()
assert solver.findMedianSortedArrays([1, 3], [2]) == 2
assert solver.findMedianSortedArrays([1, 3, 5], [2]) == 2.5
assert solver.findMedianSortedArrays([1], [2]) == 1.5
assert solver.findMedianSortedArrays([1, 3, 5], [2, 6]) == 3
assert solver.findMedianSortedArrays([1, 3, 3, 10, 11], [1, 2]) == 3
