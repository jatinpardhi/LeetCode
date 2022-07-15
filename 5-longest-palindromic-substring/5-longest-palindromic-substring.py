class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=''
        resl=0
        for i in range(len(s)):
            
            l=i
            r=i
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if (r-l+1)>resl:
                    resl=(r-l+1)
                    res=s[l:r+1]
                    #res=s[l]+res+s[r]
                l-=1
                r+=1
            l=i
            r=i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if(r-l+1)>resl:
                    resl=(r-l+1)
                    res=s[l:r+1]
                    #res=s[l]+res+s[r]
                l-=1
                r+=1
        return res
        
                
        