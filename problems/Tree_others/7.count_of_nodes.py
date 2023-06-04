class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def countOfNodes(self, root: TreeNode) -> int:
        
        def traverse(node):
            if not node:
                return 0
            
            left_node = traverse(node.left)
            right_node = traverse(node.right)

            return left_node + right_node + 1

        return traverse(root)