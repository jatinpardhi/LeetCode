class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        currMax=1
        currMin=1
        
        for n in nums:
            temp=currMax*n
            currMax=max(currMax*n,currMin*n,n)
            currMin=min(temp,currMin*n,n)
            res=max(res,currMax,currMin)
        return res
            
        
        '''
        maxProduct=-1000000
        currProduct=1
        
        for x in nums:
            currProduct*=x
            if currProduct>maxProduct:
                maxProduct=currProduct
            if currProduct<=0:
                currProduct=1
        return maxProduct
        '''