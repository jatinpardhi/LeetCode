
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        msf=prices[0]
        for i in range(1,len(prices)):
            #if prices[i]<msf:
            msf=min(msf,prices[i])
            maxProfit=max(maxProfit,prices[i]-msf)
        return maxProfit
                
            
            
   