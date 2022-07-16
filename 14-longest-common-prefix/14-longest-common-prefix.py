class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        re=''
        for i in range(len(strs[0])):
            for x in strs:
                if i==len(x) or x[i]!=strs[0][i]:
                    return re
            re+=strs[0][i]
        return re

      
    
    
    