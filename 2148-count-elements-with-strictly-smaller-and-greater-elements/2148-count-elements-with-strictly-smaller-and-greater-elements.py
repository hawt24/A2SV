class Solution:
    def countElements(self, nums: List[int]) -> int:
        if len(set(nums))==1:
            return 0
        ans = len(nums)-(nums.count(max(nums))+nums.count(min(nums)))
        return ans

    

        