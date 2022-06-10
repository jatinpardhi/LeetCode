from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s=list(s)
        l=len(s)
        d1=defaultdict(lambda:0)
        start=0
        end=0
        maxLength=0
        count=0
        
        while(end<l):
            d1[s[end]]+=1
            count+=1
            while d1[s[end]]>1:
                d1[s[start]]-=1
                start+=1
                count-=1
            maxLength=max(maxLength,count)
            end+=1
        return maxLength
            
                
            
            
            
            
            