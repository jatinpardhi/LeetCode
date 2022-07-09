# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

        def height(root,h,maxd):
            if root==None:
                return 0
            lh=height(root.left,h+1,maxd)
            rh=height(root.right,h+1,maxd)
            maxd[0]=max(maxd[0],lh+rh)
            return max(lh,rh)+1
        
        maxd=[-100000]
        
        def preorder(root,maxd):
            if root==None:
                return 0
            
            lh=height(root.left,maxd+1)
            rh=height(root.right,maxd+1)
            maxd=max(maxd,(lh+rh))
            preorder(root.left,maxd)
            preorder(root.right,maxd)
            return maxd
        
        height(root,0,maxd)
        return maxd[0]
        