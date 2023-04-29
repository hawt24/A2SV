class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        there is at least 1 cell in this island so start my count=1
        
        """
        def dfs(i,j):
            direcctions=[(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            cnt=1
            grid[i][j]="#"  #for avoding agin visiting
            for (r,c) in direcctions:
                if (0 <= r < len(grid)) and (0 <=c< len(grid[0])) and grid[r][c]==1:
                    cnt+=dfs(r,c)
            return cnt
                    
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    ans=max(ans,dfs(i,j))
        return ans