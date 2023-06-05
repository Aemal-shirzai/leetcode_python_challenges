from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isIdentical(root, subRoot):
            if not root and not subRoot:
                return True
            
            if not root or not subRoot:
                return False
            
            if root.val == subRoot.val:
                return isIdentical(root.left, subRoot.left) and isIdentical(root.right, subRoot.right)


        def helper(root, subRoot):
            if not subRoot:
                return True
            elif not root:
                return False
            
            if root.val == subRoot.val:
                if isIdentical(root, subRoot):
                    return True

            return helper(root.left, subRoot) or helper(root.right, subRoot)
        
        return helper(root, subRoot)