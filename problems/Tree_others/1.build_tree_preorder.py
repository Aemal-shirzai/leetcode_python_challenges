from typing import Optional, List


"""
    Solution: preorder means first finish left nodes and then start for right node.

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createTree(self, data: List[int]) -> TreeNode:
        current_index = -1

        def build():
            nonlocal current_index
            current_index += 1
            if data[current_index] == -1 or current_index == len(data):
                return

            node = TreeNode(val=data[current_index])
            node.left = build()
            node.right = build()

            return node

        return build()


obj = Solution()
root = obj.createTree([1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1])