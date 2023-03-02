class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top=list(accumulate(grid[0]))
        bott=list(accumulate(grid[1]))
        ans=float("inf")
        for i in range(len(grid[0])):
            topChoice=top[-1]-top[i]
            botChoice=bott[i-1] if i>0 else 0
            secRob=max(topChoice,botChoice)
            ans=min(ans,secRob)
        return ans
        

            
            
     
    