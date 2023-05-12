from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        to_be_replace_index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[to_be_replace_index] = nums[i]
                to_be_replace_index += 1
        return to_be_replace_index
    

        # Solution 2: Slow
        # unique_list = []
        # counter = 0
        # numbe_of_iterations = len(set(nums))
        # while counter < numbe_of_iterations:
        #     element = nums[counter]
        #     if element not in unique_list:
        #         unique_list.append(element)
        #         counter += 1
        #         continue  
        #     nums.pop(counter)
        #     nums.append('_')
        # return counter
    

