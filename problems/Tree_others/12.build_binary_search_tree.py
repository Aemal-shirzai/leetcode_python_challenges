from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildBinarySearchTree(self, data: List) -> TreeNode:
        root = None
        
        def build(root, val):
            # Build root node
            if not root:
                return TreeNode(val)
            
            # Build childrens
            if val < root.val:
                root.left = build(root.left, val)
            else:
                root.right = build(root.right, val)
            
            return root


        for val in data:
            root =  build(root, val)     

        return root

obj = Solution()
# root = obj.buildBinarySearchTree([5,1,3,4,2,7])
root = obj.buildBinarySearchTree([8,5,10,11,6,3,1,14,4])

