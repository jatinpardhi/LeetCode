# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def height(root):
            if root==None:
                return 0
            
            if root.left==0 and root.right==0:
                return 1
            return 1+ max(height(root.left),height(root.right))
        return height(root)
        