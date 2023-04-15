class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        temp=sorted(nums)
        if temp[-2]*2<=temp[-1]: 
            return nums.index(temp[-1])
        return -1