class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        res=nums[0]
        start=0
        end=len(nums)-1
        
        while(start<=end):
            
            if nums[start]<nums[end]:
                res=min(nums[start],res)
                break
            mid=(start+end)//2
            res=min(res,nums[mid])
            if nums[mid]>=nums[start]:
                start=mid+1
            else:
                end=mid-1
        return res
        
        '''
        start=0
        end=len(nums)-1
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return min(nums)
        while(start<end):
            mid=(start+end)//2
            if nums[start]<nums[end] :
                return nums[start]
            if nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]:
                return nums[mid]
            if nums[mid]>nums[end]:
                start=mid+1
            else:
                end=mid-1
        '''