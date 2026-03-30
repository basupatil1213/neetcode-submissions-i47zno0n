# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if q.val < p.val:
            p, q = q, p
        
        def helper(node, p, q):
            if p.val <= node.val and q.val >= node.val:
                return node
            
            return helper(node.left, p, q) if (p.val < node.val and q.val < node.val) else helper(node.right, p, q)
        
        return helper(root, p, q)
        