# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        q=collections.deque()
        q.append(root)
        
        while q:
            q1=len(q)
            k=[]
            for i in range(q1):
                xx=q.popleft()
                if xx:
                    k.append(xx.val)
                    if xx.left:
                        q.append(xx.left)
                    if xx.right:
                        q.append(xx.right)
            if k!=[]:
                res.append(k)
        return res
        
        