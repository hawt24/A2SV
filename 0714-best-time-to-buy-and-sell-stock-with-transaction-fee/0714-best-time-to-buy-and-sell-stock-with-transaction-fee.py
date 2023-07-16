class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        
        def dfs(i, buying):
            if (i, buying) in memo:
                return memo[(i, buying)]
            
            if i == len(prices):
                return 0
            
            if buying:
                buy = dfs(i+1, False) - prices[i] - fee
                not_buy = dfs(i+1, True)
                memo[(i, buying)] = max(buy, not_buy)
            else:
                sell = dfs(i+1, True) + prices[i]
                not_sell = dfs(i+1, False)
                memo[(i, buying)] = max(sell, not_sell)
            
            return memo[(i, buying)]
        
        return dfs(0, True)
            
        
                    
                        
                
                
        
        