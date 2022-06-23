# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def sameis(p,q):
            if p==None and q==None:
                return True
            if (p==None and q!=None) or (p!=None and q==None):
                return False
            if p.val!=q.val:
                return False
            if sameis(p.left,q.left) and sameis(p.right,q.right):
                return True
        return sameis(p,q)
            
            
        