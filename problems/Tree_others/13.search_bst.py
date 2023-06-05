class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode, key) -> bool:
        
        def search(node, key):
            if not node:
                return False

            if key == node.val:
                return True    
        
            if key < node.val:
                return search(node.left, key)
            elif key > node.val:
                return search(node.right, key)


        return search(root, key)