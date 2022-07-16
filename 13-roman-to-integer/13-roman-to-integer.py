class Solution:
    def romanToInt(self, s: str) -> int:
        d1={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res=0
        for i in range(len(s)):
            if i+1<len(s) and d1[s[i]]<d1[s[i+1]]:
                res-=d1[s[i]]
            else:
                res+=d1[s[i]]
        return res
                
        