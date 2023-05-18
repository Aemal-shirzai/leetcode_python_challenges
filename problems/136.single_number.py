from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return next(filter(lambda num: nums.count(num) == 1, nums))
        