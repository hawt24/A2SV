class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}
        coins.sort(reverse=True)
        def dfs(val):
            
            if val==0:
                return 0
            if val<0:
                return float("inf")
            if val in memo:
                return memo[val]
            
            step=float("inf")
            for i in  coins:
                if amount-i>=0:
                    step=min(step,dfs(val-i))
                    
            memo[val]=step+1
            return step+1
        ans=dfs(amount)
        if ans!= float("inf"):
            return ans
        else:
            return -1
            
        
            

            
        
            
        
        
        

        
        