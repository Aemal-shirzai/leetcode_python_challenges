from typing import List

"""
    Solution: Use Queue FIFO technique
        1. Add node to queue
        2. Add null value for seperating the levels
        3. Remove node from queue
        4. Add node left and right childrens
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverseTree(self, root: TreeNode) -> List[int]:
        if not root:
            return None

        queue = []
        final_result = []
        current_level = []
        queue.append(root)
        queue.append(None)

        while len(queue):
            current_element = queue.pop(0)
            if current_element:
                current_level.append(current_element.val)
                if current_element.left:
                    queue.append(current_element.left)
                if current_element.right:
                    queue.append(current_element.right)
            else:
                final_result.append(current_level)
                current_level = []
                if not len(queue):
                    break
                queue.append(None)
        return final_result

