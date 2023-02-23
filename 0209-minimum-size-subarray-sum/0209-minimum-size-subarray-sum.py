class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,sum_n=0,0
        ans=float("inf")
        for r in range(len(nums)):
            sum_n+=nums[r]
            while sum_n>=target:
                ans=min(r-l+1,ans)
                sum_n-=nums[l]
                l+=1
        if ans==float("inf"):
            return 0
        return ans
        
   
        
        