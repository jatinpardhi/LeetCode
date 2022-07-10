class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        re=[root.val]
        def maxsum(root):
            
            if root==None:
                return 0
            leftmax=maxsum(root.left)
            rightmax=maxsum(root.right)
            leftmax=max(0,leftmax)
            rightmax=max(0,rightmax)
            
            re[0]=max(re[0],root.val+leftmax+rightmax)
            return root.val+max(leftmax,rightmax)
        maxsum(root)
        return re[0]
        