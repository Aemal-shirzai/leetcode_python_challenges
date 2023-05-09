class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        to_be_replace_index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[to_be_replace_index] = nums[i]
                to_be_replace_index += 1
        return to_be_replace_index