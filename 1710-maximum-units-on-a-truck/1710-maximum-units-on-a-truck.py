class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1] ,reverse=True)
        #print(boxTypes)
        ans=0
        for x in boxTypes:
            if x[0]<truckSize:
                ans+=(x[0]*x[1])
                truckSize-=x[0]
            else:
                ans+=(truckSize*x[1])
                break
        return ans
                
        
        