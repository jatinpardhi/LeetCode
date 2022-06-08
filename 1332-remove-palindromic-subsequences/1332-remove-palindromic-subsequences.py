class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s)==0:
            return 0
        if s==s[::-1]:
            return 1
        x=s.count('a')
        y=s.count('b')
        
        if x>0 and y>0:
            return 2
        return 1
        