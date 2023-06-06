from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def traverse(node, res=[]):
            if not node:
                return 

            traverse(node.left)
            res.append(node.val)
            traverse(node.right)

            return res

        return traverse(root)