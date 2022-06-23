# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root!=None and root.left==None and root.right==None:
            return root
        
        def invert(root):
            if root==None:
                return 
            if root.left==None and root.right==None:
                return
            invert(root.left)
            invert(root.right)
            temp=root.right
            root.right=root.left
            root.left=temp
            return root
        return invert(root)
            