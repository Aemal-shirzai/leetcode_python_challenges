from typing import Optional, List


"""
    Convert sorted array to height balanced binary search tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root_index = len(nums) // 2
        root = None
        if root_index:
            root = TreeNode(nums[root_index])

        def generate_tree(nums):
        
            if not nums:
                return None
            
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            
            root.left = generate_tree(nums[:mid])
            root.right = generate_tree(nums[mid+1:])
            
            return root
        
        return generate_tree(nums)
        

             