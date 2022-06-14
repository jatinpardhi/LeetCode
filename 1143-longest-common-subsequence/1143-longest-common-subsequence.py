class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        word1=text1
        word2=text2
        m=len(word1)
        n=len(word2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        
        return dp[-1][-1]
        
        
        '''
        m=len(text1)
        n=len(text2)
        dp=[[-1]*(n+1)]*(m+1)
        #print(dp)
        def helper(text1,text2,index1,index2):
            if index1==len(text1) or index2==len(text2):
                return 0
            if dp[index1][index2]>=0:
                return dp[index1][index2]
            if text1[index1]==text2[index2]:
                dp[index1][index2]= 1+helper(text1,text2,index1+1,index2+1)
            else:
                dp[index1][index2]= max(helper(text1,text2,index1+1,index2),helper(text1,text2,index1,index2+1))
            return dp[index1][index2]
        return helper(text1,text2,0,0)
           ''' 
        