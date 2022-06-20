class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            n=i
            count=0
            while(n):
                if n&1==1:
                    count+=1
                n=n>>1
            ans.append(count)
        return ans
        
        