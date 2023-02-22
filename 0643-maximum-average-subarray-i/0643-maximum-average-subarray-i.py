class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total=sum(nums[:k])
        ans=total
        for i in range(len(nums)-k):
            total-=nums[i]
            total+=nums[k+i]
            ans=max(ans,total)
        return ans/k
        
      
    