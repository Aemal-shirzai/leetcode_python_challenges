from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total_sum = 0
        def find_sum(node):
            nonlocal total_sum
            if not node:
                return
                
            # Case 1: if range includes both left and right sub trees.
            if low <= node.val <= high:
                find_sum(node.left)
                total_sum += node.val
                find_sum(node.right)
            elif high <= node.val: # go to left 
                find_sum(node.left)
            else: # go to right
                find_sum(node.right)

            return total_sum

        return find_sum(root)