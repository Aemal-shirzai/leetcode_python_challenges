from typing import List


"""
    Solution: preorder means first finish left nodes and then start for right node.

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverseTree(self, root: TreeNode) -> List[int]:
        data = []
        
        def traverse(node):
            if not node:
                data.append(-1)
                return
            data.append(node.val)
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        return data