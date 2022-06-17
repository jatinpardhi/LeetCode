
from collections import defaultdict
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        camera=[]
        def helper(node,parent):
            if node!=None:
                
                helper(node.left,node)
                helper(node.right,node)
                
                if (parent==None and d1[node]==0) or d1[node.left]==0 or d1[node.right]==0:
                    camera.append(1)
                    d1[node]=1
                    d1[node.left]=1
                    d1[node.right]=1
                    d1[parent]=1
            return camera
        
        if root==None:
            return 0
        d1=defaultdict(lambda:0)
        d1[None]=1

        helper(root,None)
        return len(camera)
    
        
       
                
                
                
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        d1=defaultdict(lambda:0)
        def helper(root):
            
            if root.left==None and root.right==None:
                return 0
            
            if root.left!=None:
                leftc=helper(root.left)
            if root.right!=None:
                rightc=helper(root.right)
         ''' 
            
            
                
            
            
        