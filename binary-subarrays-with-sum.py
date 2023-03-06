class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count=0
        preSum=0
        dic={}
        for i in nums:
            if preSum in dic:
                dic[preSum]+=1
            else:
                dic[preSum]=1
            preSum+=i
         
            if (preSum-goal) in dic:
                count+=dic[preSum-goal]
        return count