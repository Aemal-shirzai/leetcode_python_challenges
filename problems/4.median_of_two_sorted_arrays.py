from typing import List


"""
How to find Median:
    1. If item counts is odoo: The middle element is the median.
    2. If item counts are even: The sum of middle and middle + 1 / 2 is the median.
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = [*nums1, *nums2]
        nums3.sort()
        length = len(nums3)
        if length % 2 == 0:
            median = (nums3[int(length / 2) - 1] + nums3[int(length / 2)]) / 2
        else:
            median = nums3[int(length / 2)]
        return float("{:.5f}".format(median))