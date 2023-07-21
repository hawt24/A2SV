class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        seen= set()
        while len(nums) != 0:
            seen.add((min(nums) + max(nums)) / 2)
            nums = nums[1:len(nums)-1]
        return len(seen)
