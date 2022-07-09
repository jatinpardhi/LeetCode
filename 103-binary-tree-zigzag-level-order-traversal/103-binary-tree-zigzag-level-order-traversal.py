# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return
        res=[]
        q=collections.deque()
        q.append(root)
        
        while q:
            q1=len(q)
            k=[]
            for i in range(q1):
                x=q.popleft()
                k.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            res.append(k)
        for i in range(1,len(res),2):
            res[i].reverse()
        return res
            
            
        