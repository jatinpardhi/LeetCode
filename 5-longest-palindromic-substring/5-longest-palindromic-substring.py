class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=''
        resl=0
        
        for i in range(len(s)):
            l,r=i,i
            #odd length
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if (r-l+1)>resl:
                    resl=(r-l+1)
                    res=s[l:r+1]
                r+=1
                l-=1
            #even length
            l,r=i,i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if (r-l+1)>resl:
                    resl=(r-l+1)
                    res=s[l:r+1]
                r+=1
                l-=1
        return res
                
        