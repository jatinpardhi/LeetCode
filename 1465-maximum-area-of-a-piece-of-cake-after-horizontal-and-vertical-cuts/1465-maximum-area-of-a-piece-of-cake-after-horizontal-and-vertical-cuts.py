class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        #print(verticalCuts)
        horizontalCuts.extend([0,h])
        verticalCuts.extend([0,w])
        #print(verticalCuts)
        verticalCuts.sort()
        horizontalCuts.sort()
        
        xmax=0
        for i in range(len(horizontalCuts)-1):
            xmax=max(xmax,horizontalCuts[i+1]-horizontalCuts[i])
        ymax=0
        for i in range(len(verticalCuts)-1):
            ymax=max(ymax,verticalCuts[i+1]-verticalCuts[i])
        # print(verticalCuts)
        # print(horizontalCuts)
        return (xmax*ymax)%1000000007
        