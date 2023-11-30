class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 1  

            if grid[i][j] == -1:
                return 0  # Already visited

            grid[i][j] = -1  # Marking the cell as visited

            ans = 0
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for di, dj in directions:
                new_i, new_j = i + di, j + dj
                ans += dfs(new_i, new_j)

            return ans

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)
