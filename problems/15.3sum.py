from typing import List
"""
    Solution: 
        For first number just using simple loop
        for Second and third number we can use TwoSum solution.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def twoSum(num, left, right):
            if left >= right:
                return

            total_sum = num + nums[left] + nums[right]
            if total_sum == 0:
                result.append([num, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
            elif total_sum < 0:
                left += 1
            else:
                right -= 1

            return twoSum(num, left, right)

        for index, num in enumerate(nums):
            left = index + 1
            right = len(nums) - 1
            if index > 0 and num == nums[index - 1]:
                continue
            twoSum(num, left, right)

        return result