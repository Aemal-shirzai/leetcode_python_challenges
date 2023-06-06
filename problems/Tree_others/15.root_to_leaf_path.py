from typing import List, Optional


"""
    Solution1:
        1. Need an arrya
        2. Add path to the array until we reach leaf node. For left and for right
        3. When its leaf node one path is complete. 
        5. when going back then remove the current element.

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rootToLeafPath(self, root: TreeNode) -> List:
        paths = []
        def find_path(node, current_path=[]):
            if not node:
                return
            
            current_path.append(node.val)

            # Option one
            if not node.left and not node.right:
                paths.append([*current_path])
            else:
                find_path(node.left)
                find_path(node.right)
            current_path.pop()

            
            # Option 2
            # find_path(node.left)
            # if not node.right:
            #     paths.append([*current_path])
            # else:
            #     find_path(node.right)
                
            # current_path.pop()

        find_path(root)
        return paths 