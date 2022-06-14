class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        s1 = word1 ; s2 = word2
        
        dp = [ [0]*(len(s2)+1) for _ in range(len(s1)+1) ]
        
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        return len(s1) + len(s2) - (dp[-1][-1] * 2)
        
        '''
        
        m=len(word1)
        n=len(word2)
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        
        return m-dp[i][j]+n-dp[-1][-1]
                
        '''
        