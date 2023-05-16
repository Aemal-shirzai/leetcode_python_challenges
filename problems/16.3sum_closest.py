from typing import List

"""
    Solution: 
        For first number just using simple loop
        for Second and third number we can use TwoSum solution and find the smallest difference.
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = None
        min_difference = float('inf')

        def twoSum(num, left, right):
            
            nonlocal closest
            nonlocal min_difference

            if left >= right:
                return

            total_sum = num + nums[left] + nums[right]

            if total_sum == target:
                closest = total_sum
                return
            
            difference = abs(target - total_sum)
            if difference < min_difference:
                min_difference = difference
                closest = total_sum

            if total_sum < target:
                left += 1
            else:
                right -= 1

            return twoSum(num, left, right)

        for index, num in enumerate(nums):
            left = index + 1
            right = len(nums) - 1

            if index != 0 and nums[index] == nums[index-1]:
                continue 

            twoSum(num, left, right)

        return closest