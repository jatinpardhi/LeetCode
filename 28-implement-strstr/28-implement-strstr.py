class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l=0
        r=len(needle)
        flag=0
        while(l<len(haystack)):
           # print(haystack[:r])
            if haystack[l:r]==needle:
                flag=1
                break
            else:
                l+=1
                r+=1
        if flag==0:
            return -1
        return l
            
        
        
        
        
        
        
        
       
        