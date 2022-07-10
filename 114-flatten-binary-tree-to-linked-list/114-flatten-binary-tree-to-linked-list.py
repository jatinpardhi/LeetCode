# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
    def __init__(self):
        self.prev = None
    
    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root
        
        '''
        def findlastnode(root):
            if root.left==None and root.right==None:
                return root
            
            if root.left:
                x=findlastnode(root.left)
            else:
                x=findlastnode(root.right)
        
                
            
        curr=root  
        while curr:
            if curr.left:
              
                lastnode=findlastnode(curr.left)
                print(lastnode)
                x=curr.right
                curr.right=curr.left
                lastnode.right=x
            curr=curr.right
    
        return root
        '''