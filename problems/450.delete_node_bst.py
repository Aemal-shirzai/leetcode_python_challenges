from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def get_inorder_successor(node):
            while node.left != None:
                node = node.left

            return node

        def delete(node, key):
            if not node:
                return node
                
            if key < node.val:
                node.left = delete(node.left, key)
            elif key > node.val:
                node.right = delete(node.right, key)
            else:
                # Case that node is leaf
                if not node.left and not node.right:
                    return None
                
                # Case it has one child
                if not node.right:
                    return node.left
                
                if not node.left:
                    return node.right
                
                # Case 3: deleted node has 2 childs: Right node left most node
                inorder_successor = get_inorder_successor(node.right)
                node.val = inorder_successor.val
                node.right = delete(node.right, inorder_successor.val)
                

            return node

        return delete(root, key)