class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # num=set(nums)
        # for i in range(1,5*10**5):
        #     if i not in num:
        #         return i
        nums.sort()
        num = 1
        for i in range(len(nums)):
            if num == nums[i]:
                num += 1
                print(num)
        return num

