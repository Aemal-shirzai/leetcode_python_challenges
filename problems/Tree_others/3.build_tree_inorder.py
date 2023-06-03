from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createTree(self, data: List[int]) -> TreeNode:
        def build(inorder):
            if not inorder:
                return

            current_order_root = len(inorder) // 2
            root = TreeNode(val=inorder[current_order_root])

            root.left = build(inorder[:current_order_root])
            root.right = build(inorder[current_order_root + 1:])

            return root 

        return build(data)            

obj = Solution()
# root = obj.createTree(['D', 'B', 'E', 'A', 'F', 'C'])
# root = obj.createTree([4, 2, 5, 1, 3, 6])
root = obj.createTree([9,3,15,20,7])
