'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        l1=len(s1)
        l2=len(s2)
        if l1>0 and l2>0:
            l3=len(s3)-2
        else:
            l3=len(s3)-1
        flag=0
        i,j=0,0
        while((i+j)<l3):
            if (s1[i]!=s3[i+j] or i>=len(s1)) and (j>=len(s2) or s2[j]!=s3[i+j]):
                print('hi')
                flag=1
                break
            elif s1[i]==s3[i+j]:

                i+=1
            elif s2[j]==s3[i+j]:
                j+=1
        if flag==1:
            return False
        return True

      '''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3)>len(s1)+len(s2) or len(s3)<len(s1)+len(s2):
            return False
        @cache
        def dfs(i,j):
            if i== len(s1) and  j==len(s2):
                return True
            c_s1 , c_s2 = False, False
            
            if i<len(s1) and s1[i]==s3[i+j]:
                c_s1 = dfs(i+1,j)
            if j<len(s2) and s2[j]==s3[i+j]:
                c_s2 = dfs(i,j+1)
                
            return c_s1 or c_s2
        
        return dfs(0,0)
        