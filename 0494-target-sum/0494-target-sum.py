class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}
        def dp(idx,total):
            cnt=0
            if idx==len(nums):
                return 1 if target==total else 0
            if (idx,total) in memo:
                return memo[(idx,total)]
    
            memo[(idx,total)]=dp(idx+1,total-nums[idx])+dp(idx+1,total+nums[idx])
        
            return memo[(idx,total)]
        return dp(0,0)
        