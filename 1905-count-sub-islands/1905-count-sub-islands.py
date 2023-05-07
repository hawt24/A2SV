class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ans=0
        
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(i,j):
            
            if i<0 or j<0 or i>=len(grid1) or j>=len(grid1[0]) or  grid2[i][j]!=1:
                return
            grid2[i][j]=0
            for (r,c) in direction:
                dfs(r+i,c+j)
        
        
        
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j]==1 and grid1[i][j]==0:
                    dfs(i,j)
                    
                    
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j]==1:
                    dfs(i,j)
                    ans+=1
        return ans
        
        
        