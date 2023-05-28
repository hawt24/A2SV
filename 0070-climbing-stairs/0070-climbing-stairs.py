class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo={}
        def climb(label):
            if label==n:
                return 1
            if label==n+1:
                return 0
            if label not in memo:
                memo[label]=climb(label+1)+climb(label+2)
            return memo[label]
        
        
        return climb(0)
        
            
            
            
            
