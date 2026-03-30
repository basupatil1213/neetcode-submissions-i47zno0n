# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(min_val, node, max_val):
            if not node:
                return True
            
            if not min_val < node.val < max_val:
                return False
            
            return helper(min_val, node.left, node.val) and helper(node.val, node.right, max_val)

        return helper(float('-inf'), root, float('inf'))
        