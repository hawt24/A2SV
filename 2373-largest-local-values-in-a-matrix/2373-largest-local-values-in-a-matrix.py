class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)-2
        ans=[]
        for i in range(n):
            ans.append([0]*n)
            print(ans)
        for  i in range(n):
            for j in range(n):
                ans[i][j]=max(grid[i][j],grid[i][j+1],grid[i][j+2],
                      grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2],
                      grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2])
          
        return ans
        
        
        
        