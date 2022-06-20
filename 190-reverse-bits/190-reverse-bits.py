class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for i in range(32):
            
            he=n>>i &(1)
            res=res|(he<<(31-i))
        return res
        
        
        
        