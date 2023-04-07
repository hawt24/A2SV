class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        for i in range(len(nums)):
            if cnt[nums[i]]==1:
                return nums[i]