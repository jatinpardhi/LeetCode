# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d1=defaultdict(lambda:[])
        def height(root,c):
            if root==None:
                return 0
            d1[c].append(root.val)
            height(root.left,c+1)
            height(root.right,c+1)
        c=0
        height(root,c)
        return list(d1.values())
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        def height(root,h):
            if(root==None):
                return 0
            hleft=height(root.left,h+1)
            hright=height(root.right,h+1)
           # print(max(hleft,hright)+1)
            return(max(hleft,hright)+1)
            
        def lorder(root,a,count):
            if(root==None):
                return
            a[count].append([root.val])
            lorder(root.left,a,count+1)
            lorder(root.right,a,count+1)
            return a
        x=0
        h=height(root,x)
        a=defaultdict(lambda:[])
        ans=[]
        
        count=0
        lorder(root,a,count)
        for x in a:
            ans.append(x)
        return ans
        '''
            
        