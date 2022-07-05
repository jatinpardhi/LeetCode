
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d1=set()
        for x in nums:
            d1.add(x)
        maxCount=0
        for x in nums:
            if x-1 in d1:
                continue
            else:
                count=1
                k=x+1
                while k in d1:
                    count+=1
                    k+=1
                maxCount=max(maxCount,count)
        return maxCount
                
                    
                
        
        
        
            