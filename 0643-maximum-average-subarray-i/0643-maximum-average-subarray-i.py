class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_=sum(nums[:k])
        ans=sum_
        for i in range(len(nums)-k):
            sum_-=nums[i]
            sum_+=nums[i+k]
            ans=max(ans,sum_)
        return ans/k
            
        

        