class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        for i in range(len(triangle)-1,0,-1):
            x=triangle[i]
            for j in range(len(x)-1):
                triangle[i-1][j]+=min(triangle[i][j],triangle[i][j+1])
        return triangle[0][0]
                
       
            
            
            
        