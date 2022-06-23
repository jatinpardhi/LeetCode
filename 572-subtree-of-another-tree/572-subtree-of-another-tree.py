# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameis(p,q):
            if p==None and q==None:
                return True
            if (p==None and q!=None) or (p!=None and q==None):
                return False
            if p.val!=q.val:
                return False
            if sameis(p.left,q.left) and sameis(p.right,q.right):
                return True
        
        ans=[]
        def x(root,subRoot):
            
            if root==None and subRoot==None:
                return True
            if (root==None and subRoot!=None) or (root!=None and subRoot==None):
                return False
            if root.val==subRoot.val:
                if sameis(root,subRoot):
                    xx=True
                    ans.append(xx)
            x(root.left,subRoot)
            x(root.right,subRoot)
        x(root,subRoot)
        if len(ans)>0:
            return True
        else:
            return False
            
        