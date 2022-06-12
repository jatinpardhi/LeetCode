from collections import defaultdict
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        d1=defaultdict(lambda:0)
        start=0
        currSum=0
        maxSum=-1000
        for i in range(len(nums)):
            if nums[i] in d1:
                while start<=i and d1[nums[i]]==1 :
                    currSum-=nums[start]
                    d1[nums[start]]=0
                    start+=1
                    #print(d1[nums[start]])
                    #print(d1)
                #print(currSum)
                d1[nums[i]]+=1
                currSum+=nums[i]
                
            else:
                d1[nums[i]]+=1
                currSum+=nums[i]
            maxSum=max(maxSum,currSum)
        return maxSum
                    
                
                
        
        
        