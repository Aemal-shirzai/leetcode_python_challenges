from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
      
class Solution:
    def printInRange(self, root: TreeNode, low: int, high: int) -> List:
        def print_val(node, range_data=[]):
            if not node:
                return range_data
        
            # Case 1: if range includes both left and right sub trees.
            if low <= node.val <= high:
                print_val(node.left)
                range_data.append(node.val)
                print_val(node.right)
            elif high < root.val: # go to left 
                print_val(node.left)
            elif low > root.val: # go to right
                print_val(node.right)

            return range_data
        return print_val(root)