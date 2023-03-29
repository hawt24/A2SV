class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        '''calculate each row ,col and diagonal then cheak all are equal'''
        ans=0
        for r in range(len(grid)-2):
            for c in range(len(grid[0])-2):
                r1=sum(grid[r][c:c+3])
                r2=sum(grid[r+1][c:c+3])
                r3=sum(grid[r+2][c:c+3])
                c1= grid[r][c] + grid[r+1][c] + grid[r+2][c]
                c2=grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1]
                c3=grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2]
                diagonal=grid[r][c]+grid[r+1][c+1]+grid[r+2][c+2]
                diagonal1=grid[r+2][c] + grid[r+1][c+1] + grid[r][c+2]
                value=set(grid[r][c:c+3] +grid[r+1][c:c+3] + grid[r+2][c:c+3])
                if r1 == r2 == r3 == c1 == c2 == c3 == diagonal == diagonal1 and len(value)==9 and min(value)==1 and max(value)==9:
                    ans+=1
        return ans
                
                