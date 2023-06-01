class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        memo={}
        def dp(idx):
            if idx==0:
                return nums[0]
            if idx==1:
                return max(nums[1],nums[0])
            if idx not in memo:
                memo[idx]=max(dp(idx-1),dp(idx-2)+nums[idx])
            return memo[idx]
        ans=dp(len(nums)-2)

        memo={}
        def dp(idx):
            if idx==1:
                return nums[1]
            if idx==2:
                return max(nums[1],nums[2])
            if idx not in memo:
                memo[idx]=max(dp(idx-1),dp(idx-2)+nums[idx])
                temp1.append(memo[idx])
            return memo[idx]
        temp1=[]
        ans1=dp(len(nums)-1)
    
        
        return max(ans1,ans)
        
        
    
            
    
        
        