class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        visited=set()
    
        def dfs(i,j):
            nonlocal visited
            if (i,j) in visited:
                return 0
            if i<0 or j<0 or j==len(grid[0]) or i==len(grid) or grid[i][j]==0:
                return 1
            
            visited.add((i,j))
            return dfs(i+1,j) + dfs(i- 1, j) + dfs(i,j+1) + dfs(i,j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return dfs(i,j)

            
            