class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        dp = {}
        res = 1
        
        for word in sorted(words, key=len):
            
            dp[word] = 1
            
            for i in range(len(word)):
                
                new_word = word[:i] + word[i+1:]
                
                if new_word in dp:
                    dp[word] = max(dp[word], dp[new_word]+1)
                    
                res = max(res, dp[word])
        
        return res



'''
from collections import defaultdict
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        #print(words)
        res=0
        d1=defaultdict(lambda:0)
        
        for x in words:
            d1[x]=1
            for i in range(len(x)):
                curr=x
                nextt=curr.replace(curr[i],'')
                #print(nextt)
                if d1[nextt]>0:
                    d1[x]=max(d1[x],d1[nextt]+1)
            res=max(res,d1[x])
        return res
        
   '''     