class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            a=nums[-1]*nums[-2]
            b=nums[0]*nums[1]
        return a-b