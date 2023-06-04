class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution O(N^2): because every node is visited twice one to find diameter and 2nd to find height
"""
    Diameter means: longest path between two nodes
    Solution:
        1. Left subtree diameter
        2. Right subtree diameter
        3. Height of left subtree and height of right sub tree
        4. find maximum between the above three. 
            a. If left subtree diameter is max: it means the longest diameter is in left subtree and not crossing the root
            b. If Right subtree diameter is max: it means the longest diameter is in right subtree and not crossing the root
            c. If point 3 is max it means the diameter is crossing the root.
"""

class Solution:
    def findDiameter(self, root: TreeNode) -> int:
        
        def heightOfNodes(node: TreeNode) -> int:
            if not node:
                return 0
            
            left_node = heightOfNodes(node.left)
            right_node = heightOfNodes(node.right)

            return max(left_node, right_node) + 1
        

        def diameter(node):
            if not node:
                return 0
            
            diam1 = diameter(node.left)
            diam2 = diameter(node.right)
            diam3 = heightOfNodes(node.left) + heightOfNodes(node.right) + 1

            return max(diam3,  max(diam1, diam2))
    
        return diameter(root)