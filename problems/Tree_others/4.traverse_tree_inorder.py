from typing import List

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
                    return
                traverse(node.left)
                data.append(node.val)
                traverse(node.right)

            traverse(root)
            return data