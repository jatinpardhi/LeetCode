# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lca(root,p,q):
            if root==None:
                return None
            if root.val==p.val or root.val==q.val:
                return root
            la=lca(root.left,p,q)
            ra=lca(root.right,p,q)
            
            if la and ra:
                return root
            elif la:
                return la
            elif ra:
                return ra
        return(lca(root,p,q))