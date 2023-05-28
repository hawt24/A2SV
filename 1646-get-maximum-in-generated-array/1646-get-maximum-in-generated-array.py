class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        
        nums = [0] * (n+1)
        nums[1] = 1
        
        def dp(i):
            if i > n:
                return

            if i % 2 == 0:
                nums[i] = nums[i//2]
            else:
                nums[i] = nums[(i-1)//2] + nums[(i+1)//2]
                
            dp(i+1)
        
        dp(2)
        return max(nums)
        