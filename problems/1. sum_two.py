from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        current_index = 0
        visited = {}
        while current_index < len(nums):
            current_value = nums[current_index]
            complement = target - current_value
            if complement in visited:
                return [visited[complement], current_index]
            visited[current_value] = current_index
            current_index += 1