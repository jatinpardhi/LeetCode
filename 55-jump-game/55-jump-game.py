class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        goalPost=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=goalPost:
                goalPost=i
        if goalPost==0:
            return True
        return False
        
        
        '''
        i=0
        while(i<len(nums)):
            if i==len(nums)-1:
                return True
            x=nums[i]
            if x==0:
                return False
            while(x>0):
                i+=1
                x-=1
                #print(i)
        if i<len(nums):
            return False
        else:
            return True
            
        ''' 
        