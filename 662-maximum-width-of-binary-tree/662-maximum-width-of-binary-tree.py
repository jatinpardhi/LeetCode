# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_w=1
        curr_l=[(root,1)]
        while curr_l!=[]:
            next_l=[]
            for rot,pos in curr_l:
                if rot.left:
                    next_l.append((rot.left,2*pos))
                if rot.right:
                    next_l.append((rot.right,2*pos+1))
            if next_l!=[]:
                max_w=max(max_w,next_l[-1][1]-next_l[0][1]+1)
            curr_l=next_l
        return max_w
        
        