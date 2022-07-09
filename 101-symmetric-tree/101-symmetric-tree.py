# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def check(r1,r2):
            if  not r1 and not r2:
                return True
            if r1 and r2 and r1.val==r2.val:
                return check(r1.left,r2.right) and check(r1.right,r2.left)
    
        return root==None or check(root.left,root.right)
        '''
        def isSym(L,R):
            if not L and not R: return True
            if L and R and L.val == R.val: 
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False
        return isSym(root, root)            
        '''
        