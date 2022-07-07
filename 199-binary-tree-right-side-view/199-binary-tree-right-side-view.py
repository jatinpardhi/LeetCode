# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        a=[]
        
        def rightView(root,level):
            if root==None:
                return
            if level==len(a):
                a.append(root.val)
            rightView(root.right,level+1)
            rightView(root.left,level+1)
        rightView(root,0)
        return a
        