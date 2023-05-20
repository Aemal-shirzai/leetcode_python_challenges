from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for index in range(m, m + n):
            nums1[index] = nums2[index - m]
        nums1.sort()
