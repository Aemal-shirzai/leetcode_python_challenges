from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def isIdentical(p, q):
            if not p and not q:
                return True
            
            if (not p or not q) or (p.val != q.val):
                return False
            
            return isIdentical(p.left, q.left) and isIdentical(p.right, q.right)


        return isIdentical(p, q)