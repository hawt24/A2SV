class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # base case: if starting cell is reached, return 1
        # recurrence relation: dp(i-1,j) + dp(i,j-1)
        
        memo = {}
        def dp(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            ans = dp(i+1, j) + dp(i, j+1)
            memo[(i, j)] = ans
            return ans
        
        return dp(0, 0)