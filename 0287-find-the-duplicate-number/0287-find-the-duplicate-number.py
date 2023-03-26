class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         return nums[i]
        cnt=Counter(nums)
        ans=0
        for i in range(len(nums)):
            if cnt[nums[i]]>1:
                ans=nums[i]
        return ans
            