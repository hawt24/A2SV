class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        ans=0
        for i in range(len(nums)):
            if cnt[nums[i]]>1:
                ans=nums[i]
        return ans
        