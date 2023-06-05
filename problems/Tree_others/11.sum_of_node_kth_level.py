from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverseTree(self, root: TreeNode, level: int) -> List[int]:
        
        if not root:
            return None
        elif level == 1:
            return root.val 

        queue = []
        current_level = 2
        total = 0

        queue.append(root)
        queue.append(None)

        while len(queue):
            current_element = queue.pop(0)
            if current_element:
                if current_element.left:
                    queue.append(current_element.left)
                    total += current_element.left.val if current_level == level else 0
                if current_element.right:
                    queue.append(current_element.right)
                    total += current_element.right.val if current_level == level else 0

                if current_level == level and not queue[0]:
                    break
                

            else:
                current_level += 1
                if not len(queue):
                    break
                queue.append(None)
        
        return total
