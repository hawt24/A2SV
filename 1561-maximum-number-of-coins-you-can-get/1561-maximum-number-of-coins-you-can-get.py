class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        sum_=0
        left=0
        right=len(piles)-1
        while left<right:
            sum_+=piles[right-1]
            left+=1
            right-=2
        return sum_
            
            
            