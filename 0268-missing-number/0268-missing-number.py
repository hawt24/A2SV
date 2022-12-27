class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        missed=0
        sum_=int((n*(n+1))/2) #arthematic progression
        for i in nums:
            missed+=i
        return sum_-missed
        
    
            
        
        
        