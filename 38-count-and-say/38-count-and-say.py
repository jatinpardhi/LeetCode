class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        res='1'
        for i in range(2,n+1):
            start=0
            end=0
            count=0
            curr=''
            while end<len(res):
                if res[start]==res[end]:
                    count+=1
                    end+=1
                else:
                    curr+=str(count)+str(res[start])
                    count=0
                    start=end
            curr+=str(count)+str(res[start])
            res=curr
        return res
                    
                
            
            
        